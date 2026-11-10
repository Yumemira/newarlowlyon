# Images

## Assets: mandatory image directory

Every application **must have a nonempty directory `assets/images/`** containing
at least one nonempty image file, including in subdirectories. A placeholder such
as `.gitkeep` alone does not count; Git does not retain empty directories.
Inspect the script's `image_directory` result for this automated check; it checks
presence, extension and nonzero file size, not image validity or Git tracking.
Store **all
application image resources exclusively inside `assets/images/`**, optionally in
its subdirectories. This includes raster images, SVGs, animated images, backgrounds,
illustrations, logos and source images used to generate launcher icons or splash
screens. Other directories such as `assets/icons/`, `assets/pictures/`, `images/`
or `lib/` are not permitted locations for these source image resources.

Inspect the project's first-party image resources, `pubspec.yaml`, asset references
and launcher/splash configuration; checking only declared assets is insufficient.
Generated platform resources (such as Android mipmaps and iOS asset catalogs) and
dependency/build caches are outputs, not application source image resources.
Their presence does not replace the mandatory source directory.

Report a missing `assets/images/` directory or any application source image outside
it as `FAIL`, listing the offending paths. Unverified coverage is incomplete, never
`PASS`. Report this check separately from the script's JSON counts and exit code
unless the script explicitly implements it. For check-only requests, report
violations without modifying the application. When fixes are authorized, move all
offending source images into `assets/images/` and update every affected reference
and configuration.


## Assets: mandatory maximum width

Check every image recursively under the project's `assets/`, including files not
listed in `pubspec.yaml`. Width must be **at most 512 px**; height is unrestricted.
Inspect `asset_width` findings. Unreadable images or unsupported formats require
manual verification and must not be reported as passed. For SVGs, verify intrinsic
width (including units/viewBox) manually; fonts, audio and other resources without
pixel dimensions are not subject to this limit.

When fixing an oversized image, resize it to **512 px wide**, with height
`max(1, round(original_height * 512 / original_width))`, preserving aspect ratio.
Use a proper image resampler (e.g. Pillow LANCZOS); preserve transparency, file
format and, for animations, every frame and its timing/loop settings. Do not upscale
images already within the limit, crop or stretch them. For SVGs, preserve the
viewBox and adjust intrinsic dimensions proportionally. Rerun the width check after
fixing; rebuild release artifacts when authorized and needed. Check-only requests
report violations without modifying assets; when fixes are authorized, apply this
resize rule to every violation.

