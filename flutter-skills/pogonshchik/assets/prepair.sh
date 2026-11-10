#!/bin/bash

set -e
export LC_ALL=C

echo ""
echo "🔧 Flutter App Prepair"
echo "----------------------------------------"

# === Пути к файлам ===
manifestPath="android/app/src/main/AndroidManifest.xml"
infoPlist="ios/Runner/Info.plist"
gradlePath="android/app/build.gradle.kts"

# === Удаление из .gitignore ===
echo "📁 Обновление .gitignore..."
for file in .gitignore android/.gitignore; do
  if [[ -f $file ]]; then
    sed -i '' '/key\.properties/d' "$file"
    sed -i '' '/key\.jks/d' "$file"
    echo "✅ $file обновлён"
  fi
done

# === Определение старого package ===
oldPackage=$(grep -o 'namespace *= *"[^"]*"' "$gradlePath" | sed 's/.*"\(.*\)"/\1/')
if [[ -z "$oldPackage" ]]; then
  echo "❌ Не удалось определить старый package (namespace)."
  exit 1
fi
echo "📦 Найден старый package: $oldPackage"

read -rp "Введите новый package name (оставьте пустым, чтобы оставить $oldPackage): " newPackage
newPackage=${newPackage:-$oldPackage}

if [[ "$oldPackage" == "$newPackage" ]]; then
  echo "⏭️ Package name не изменён, пропускаем замену."
else
  echo "🔄 Замена $oldPackage на $newPackage во всём проекте..."
  grep -rl "$oldPackage" android ios lib | xargs sed -i '' "s/$oldPackage/$newPackage/g"
  echo "✅ Package name обновлён"
fi

# === Определение старого названия ===
oldAppName=$(grep -o 'android:label="[^"]*"' "$manifestPath" | sed 's/android:label="//;s/"//')
if [[ -z "$oldAppName" ]]; then
  echo "❌ Не удалось определить старое название приложения."
  exit 1
fi
echo "📝 Найдено старое имя: $oldAppName"

read -rp "Введите новое название приложения (оставьте пустым, чтобы оставить $oldAppName): " newAppName
newAppName=${newAppName:-$oldAppName}

if [[ "$oldAppName" == "$newAppName" ]]; then
  echo "⏭️ Название приложения не изменено, пропускаем замену."
else
  echo "🔄 Замена имени $oldAppName на $newAppName..."
  grep -rl "$oldAppName" android ios | xargs sed -i '' "s/$oldAppName/$newAppName/g"
  echo "✅ Название приложения обновлено"
fi

# === CFBundleName (с подчёркиванием) ===
newBundleName=${newPackage//./_}
echo "🧩 Обновление CFBundleName в Info.plist..."
lineNum=$(grep -n "<key>CFBundleName</key>" "$infoPlist" | cut -d: -f1)
if [[ -n "$lineNum" ]]; then
  targetLine=$((lineNum + 1))
  sed -i '' "${targetLine}s|.*|    <string>$newBundleName</string>|" "$infoPlist"
  echo "✅ CFBundleName заменён на $newBundleName"
else
  echo "❌ CFBundleName не найден в Info.plist"
fi

# === INTERNET permission ===
if grep -q 'android.permission.INTERNET' "$manifestPath"; then
  echo "🌐 INTERNET permission уже добавлен"
else
  echo "🌐 Добавление INTERNET permission..."
  sed -i '' '/<manifest/a\
    <uses-permission android:name="android.permission.INTERNET"/>
  ' "$manifestPath"
  echo "✅ INTERNET permission добавлен"
fi

# === build.gradle.kts: добавление keyProperties ===
if grep -q 'val keyProperties' "$gradlePath"; then
  echo "📦 build.gradle.kts уже содержит ключи"
else
  echo "📦 Добавление блоков keyProperties в build.gradle.kts..."

  sed -i '' '1s;^;import java.io.File\
import java.io.FileInputStream\
import java.util.Properties\
\n;' "$gradlePath"

  sed -i '' '/android {/i\
val keyProperties = Properties().apply {\
    val keyFile = rootProject.file("key.properties")\
    if (keyFile.exists()) {\
        keyFile.inputStream().use { load(it) }\
    } else {\
        throw IllegalStateException("key.properties file not found.")\
    }\
}\
\
val detKeyAlias = keyProperties.getProperty("keyAlias")\
val detKeyPassword = keyProperties.getProperty("keyPassword")\
val detStoreFile = keyProperties.getProperty("storeFile")\
val detStorePassword = keyProperties.getProperty("storePassword")\
\
require(detKeyAlias != null) { "keyAlias not found in key.properties file." }\
require(detKeyPassword != null) { "keyPassword not found in key.properties file." }\
require(detStoreFile != null) { "storeFile not found in key.properties file." }\
require(detStorePassword != null) { "storePassword not found in key.properties file." }\
' "$gradlePath"
  echo "✅ Блоки добавлены в build.gradle.kts"
fi

# === android:label ===
if grep -q 'android:label=' "$manifestPath"; then
  echo "📝 Обновление android:label..."
  sed -i '' "s/android:label=\"[^\"]*\"/android:label=\"$newAppName\"/" "$manifestPath"
  echo "✅ android:label заменён"
fi
read -rp "🔐 Сгенерировать новый key.jks и key.properties? (y/N): " generateKeys
if [[ "$generateKeys" =~ ^[Yy]$ ]]; then
  echo ""
  echo "🧹 Проверка старых ключей..."
  if [[ -f key.jks ]]; then
    rm key.jks
    echo "🗑️ Удалён key.jks"
  fi
  if [[ -f android/key.properties ]]; then
    rm android/key.properties
    echo "🗑️ Удалён android/key.properties"
  fi

  echo ""
  echo "🔐 Генерация key.jks и key.properties..."

  random_string() {
    openssl rand -base64 48 | tr -dc 'A-Za-z0-9' | head -c "$1"
  }
  random_country() {
    iso_countries=(
      "US" "GB" "DE" "FR" "IT" "ES" "NL" "PL" "UA" "RU"
      "CN" "JP" "KR" "IN" "BR" "CA" "AU" "SE" "NO" "DK"
      "FI" "CH" "BE" "AT" "IE" "PT" "GR" "CZ" "SK" "HU"
      "RO" "BG" "HR" "SI" "LT" "LV" "EE" "IL" "TR" "SA"
      "AE" "ZA" "EG" "AR" "MX" "CL" "CO" "NZ" "SG" "TH"
      "MY" "ID" "VN" "PH" "NG" "KZ"
    )
    echo "${iso_countries[$RANDOM % ${#iso_countries[@]}]}"
  }

  storepass=$(random_string 24)
  CN=$(random_string 6)
  OU=$(random_string 4)
  O=$(random_string 5)
  L=$(random_string 7)
  S=$(random_string 6)
  C=$(random_country)

  dname="CN=$CN, OU=$OU, O=$O, L=$L, S=$S, C=$C"

  echo "📦 storepass: $storepass"
  echo "📦 dname: $dname"

  keytool -genkey -v \
    -keystore key.jks \
    -keyalg RSA \
    -keysize 2048 \
    -validity 10000 \
    -alias key \
    -storepass "$storepass" \
    -keypass "$storepass" \
    -dname "$dname"

  cat > android/key.properties <<EOF
storePassword=$storepass
keyPassword=$storepass
keyAlias=key
storeFile=../../key.jks
EOF

  echo "✅ key.jks и key.properties созданы"
else
  echo "⏭️ Пропущена генерация ключей."
fi


echo ""
echo "🎉 Подготовка завершена!"
