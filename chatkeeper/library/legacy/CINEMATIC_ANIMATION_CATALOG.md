# Cinematic Animation Catalog

> Shared ADS index of 50 production-tested motion patterns extracted from `flutterworks/kino_reforged_ios`. Use this catalog to select and adapt behavior; do not copy project-specific colors, geometry, controllers, or strings blindly.

After choosing a pattern, start implementation from [Cinematic Motion Implementation Template](CINEMATIC_MOTION_IMPLEMENTATION_TEMPLATE.md).

## Fast selection

| Need | Start with |
|---|---|
| Loading → Home reveal | `CIN-MOT-001`, `CIN-MOT-020`, `CIN-MOT-027` |
| Bottom navigation | `CIN-MOT-007`, `CIN-MOT-008`, `CIN-MOT-040` |
| Tile/page transition | `CIN-MOT-044`, `CIN-MOT-045`, `CIN-MOT-039` |
| Poster/movie detail | `CIN-MOT-024`, `CIN-MOT-025`, `CIN-MOT-026`, `CIN-MOT-038` |
| Selection/filter/search | `CIN-MOT-013`, `CIN-MOT-014`, `CIN-MOT-021`, `CIN-MOT-022`, `CIN-MOT-038` |
| Drag/drop/reorder | `CIN-MOT-048`, `CIN-MOT-049`, `CIN-MOT-050` |
| Success/result | `CIN-MOT-019`, `CIN-MOT-031`, `CIN-MOT-046` |
| Empty/error/retry | `CIN-MOT-012` plus the reverse/retry states in every timeline |

## Reusable architecture

Every robust entry follows the same separation:

```text
domain state + normalized progress
              ↓
        deterministic Timeline
              ↓
       immutable visual Frame
              ↓
 widget / painter / Hero / transition
```

### Timeline contract

- Accept normalized progress and explicit domain flags such as `armed`, `committed`, `reversing`, `retrying`, `cancelled`, and `reduceMotion`.
- Clamp external values before interpolation.
- Return a semantic phase plus visual scalar values; never mutate application state.
- Make `progress = 0`, `progress = 1`, reverse, cancel, and reduced motion deterministic.

### Frame contract

- Immutable values only: opacity, scale, offset, rotation, blur, light, grain, depth, clipping, or painter progress.
- No controller, `BuildContext`, repository, navigation, or haptic work inside a frame.
- Values that reach layout must remain bounded at every sampled progress value.

### Handoff contract

- Arm immediately before the navigation/action that needs continuity.
- Reject a second arm while active.
- Consume exactly once at the destination.
- Clear on cancel, stale route, failure, or dispose.
- If an ancestor `Hero` exists, return the visual child without creating a nested Hero.

### Quality contract

- `reduceMotion`: preserve final meaning immediately with no spatial travel.
- `weakDevice`: retain primary movement; remove grain, blur, particles, secondary rotation, and expensive paint layers.
- Pause animation controllers on inactive/paused lifecycle states and resume only when the action is still active.

## Catalog

Paths in **Source** are relative to `flutterworks/kino_reforged_ios/lib/ui/animation/`. Paths in **Test** are relative to `flutterworks/kino_reforged_ios/test/`.

| ID | Canonical name | Category | Trigger and cinematic metaphor | Reusable mechanism | Fallback | Source | Test |
|---|---|---|---|---|---|---|---|
| CIN-MOT-001 | Aperture Loading Reveal | Loading/navigation | Successful startup opens a cinema aperture into Home | One-shot handoff + phase timeline; loading owns arm, Home consumes | Jump to open/final content | `aperture_motion_timeline.dart` | `aperture_motion_test.dart` |
| CIN-MOT-002 | Blind Accept Stamp | Async commit | Accepting a blind pick aligns and stamps a decision | Commit/pending/success/failure/reverse frame machine | Opacity confirmation only | `blind_accept_motion.dart` | `blind_accept_motion_test.dart` |
| CIN-MOT-003 | Blind Backstage Crossing | Navigation/action | A hidden choice crosses behind a stage obstruction | Occlusion masks a state swap between crossing and cleared phases | Immediate swap | `blind_backstage_motion.dart` | `blind_backstage_motion_test.dart` |
| CIN-MOT-004 | Blind Burn Reset | Destructive/reset | Rejected blind pick burns away like discarded film | Burn amount + reset phase with reversible failure path | Fade out/in | `blind_burn_motion.dart` | `blind_burn_motion_test.dart` |
| CIN-MOT-005 | Blind Polaroid Develop | Reveal | A mystery recommendation ejects, develops, and seats | Multi-phase scale/opacity/development frame | Direct revealed card | `blind_polaroid_motion.dart` | `blind_polaroid_motion_test.dart` |
| CIN-MOT-006 | Blind Envelope Seal | Commit | Saved mystery choice folds and seals | Folding/sealing/set phases tied to one durable mutation | Static sealed state | `blind_seal_motion.dart` | `blind_seal_motion_test.dart` |
| CIN-MOT-007 | Bottom Nav Iris Jump | Navigation | Active tab closes like an iris, travels, then opens | From/to index handoff + close/travel/open intervals | Immediate selected tab | `bottom_nav_iris_timeline.dart` | `bottom_nav_iris_motion_test.dart` |
| CIN-MOT-008 | Bottom Nav Light Trail | Navigation feedback | Selection leaves a clipped luminous trail inside the bar | Tracking/trailing frame, container clipping, reverse/retry | Static active indicator | `bottom_nav_light_trail_timeline.dart` | `bottom_nav_light_trail_motion_test.dart` |
| CIN-MOT-009 | Collection Panorama | Horizontal exploration | Collection rail pans like one continuous widescreen scene | Scroll-offset timeline with tracking, settling, reverse and device quality | Standard scroll | `collection_panorama_motion.dart` | `collection_panorama_motion_test.dart` |
| CIN-MOT-010 | Director Film Montage | Horizontal exploration | Essential films scrub through an editing montage | Offset-derived parallax, crop and scrub frame | Flat scroll rail | `director_montage_motion.dart` | `director_montage_motion_test.dart` |
| CIN-MOT-011 | Director Portrait Focus | Hero/navigation | Director avatar focuses and crosses into biography | ID handoff + center-arc Hero + aperture painter; nested-Hero guard required | Direct destination portrait | `director_portrait_motion.dart` | `director_portrait_motion_test.dart` |
| CIN-MOT-012 | Empty Projector Standby | Empty state | Projector dims when no results remain | Commit/dimming/standby timeline with retry and reverse | Immediate empty state | `empty_projector_motion.dart` | `empty_projector_motion_test.dart` |
| CIN-MOT-013 | Filter Film Cut | Filtering | Applying filters cuts the visible reel to a new result set | One mutation, cut/settle phases, result swap under occlusion | Immediate result replacement | `filter_cut_motion.dart` | `filter_cut_motion_test.dart` |
| CIN-MOT-014 | Filter Rewind Clear | Reset | Clearing filters rewinds and erases the prior selection | Rewind/erased phases with reversible mutation | Immediate cleared state | `filter_rewind_motion.dart` | `filter_rewind_motion_test.dart` |
| CIN-MOT-015 | Gallery Frame Flip | Selection | Poster frame lifts, crosses, and seats like a physical print | Progress frame with lift/rotation/crossfade and reverse | Crossfade only | `gallery_frame_flip_motion.dart` | `gallery_frame_flip_motion_test.dart` |
| CIN-MOT-016 | Gallery Light Table | Selection/reveal | Selected poster illuminates on a curator's light table | Movie-ID handoff + illumination and seating frame | Static selected poster | `gallery_light_table_motion.dart` | `gallery_light_table_motion_test.dart` |
| CIN-MOT-017 | Genre Page Fold | Navigation | Genre card folds into its collection page | Fold/handoff timeline paired with page-fold widget; nested-Hero guard | Fade route | `genre_page_motion.dart` | `genre_page_motion_test.dart` |
| CIN-MOT-018 | Group Vote Token Flight | Social voting | A participant's vote token lifts, flies, and seats on a film | Armed token frame with bounded arc, spin, reverse and retry | Instant vote placement | `group_vote_token_motion.dart` | `group_vote_token_motion_test.dart` |
| CIN-MOT-019 | Winner Premiere | Result/success | Winning film receives curtain and marquee premiere treatment | Dimming/curtain/marquee layered frame; deterministic grain | Static winner highlight | `group_winner_premiere_motion.dart` | `group_winner_premiere_motion_test.dart` |
| CIN-MOT-020 | Home Depth Resolve | Page entrance | Header, actions, and catalog resolve as separate depth planes | One progress source split into delayed plane intervals | All planes settled | `home_depth_motion_timeline.dart` | `home_depth_motion_test.dart` |
| CIN-MOT-021 | Mood Atmosphere Wash | Selection | Mood selection washes the environment with a new atmosphere | Commit/wash/settle color-light frame; data refresh must not replay | Immediate palette change | `mood_atmosphere_motion.dart` | `mood_atmosphere_motion_test.dart` |
| CIN-MOT-022 | Mood Constellation Link | Selection/data | Selected moods connect as a constellation | Link pulses and line exposure from one deterministic frame | Static connected nodes | `mood_constellation_motion.dart` | `mood_constellation_motion_test.dart` |
| CIN-MOT-023 | Optical Depth Press | Micro-interaction | Pressed surfaces gain lens-like depth instead of a default scale | Pointer-driven tilt, scale, highlight and shadow frame | Existing bounce/tap feedback | `optical_depth_motion.dart` | `optical_depth_motion_test.dart` |
| CIN-MOT-024 | Poster Detail Hero | Hero/navigation | Poster expands continuously into Movie Detail | Handoff + custom rect tween + source/destination crossfade; nested-Hero guard | Direct route content | `poster_detail_motion.dart` | `poster_detail_motion_test.dart` |
| CIN-MOT-025 | Poster Scroll Parallax | Scroll | Detail poster moves optically against page scroll | Clamped offset-to-depth/translation frame with reverse symmetry | Fixed poster | `poster_parallax_motion.dart` | `poster_parallax_motion_test.dart` |
| CIN-MOT-026 | Poster Title Registration | Page entrance | Title locks into alignment like a film title card | Tracking/commit/reveal/typeset frame | Final title immediately | `poster_title_motion.dart` | `poster_title_motion_test.dart` |
| CIN-MOT-027 | Projector Loading Beam | Loading | Projector beam travels through staged preparation steps | Pure phase timeline for beam exposure and completion | Static branded loader/final state | `projector_motion_timeline.dart` | `projector_motion_test.dart` |
| CIN-MOT-028 | Quiz Film Progress | Progress | Quiz progress advances as film through a transport | Progress frame drives sprocket/strip travel without altering score | Static progress value | `quiz_film_progress_motion.dart` | `quiz_film_progress_motion_test.dart` |
| CIN-MOT-029 | Quiz Answer Spotlight | Answer commit | Selected answer receives a moving spotlight before reveal | Stateful commit animation synchronized with async answer; reverse/retry focus | Immediate correct/incorrect styling | `quiz_spotlight_motion.dart` | `quiz_spotlight_motion_test.dart` |
| CIN-MOT-030 | Reflection Ink Spread | Creation | Saved reflection blooms like ink into paper | Armed spread/settle frame with bounded painter radius and opacity | Immediate saved note | `reflection_ink_motion.dart` | `reflection_ink_motion_test.dart` |
| CIN-MOT-031 | Result Focus Pull | Result | Result shifts from soft focus to the chosen subject | Blur/scale/light frame with reveal and reverse phases | Sharp final result | `result_focus_motion.dart` | `result_focus_motion_test.dart` |
| CIN-MOT-032 | Roulette Mechanical Decay | Spin physics | Wheel momentum decays mechanically to a deterministic stop | Time/velocity decay frame; one spin mutation, lifecycle safe | Immediate selected result | `roulette_decay_motion.dart` | `roulette_decay_motion_test.dart` |
| CIN-MOT-033 | Roulette Focus Lock | Result | Lens focus locks onto the winning segment | Focus/scale/aperture frame following actual wheel completion | Static winner emphasis | `roulette_focus_motion.dart` | `roulette_focus_motion_test.dart` |
| CIN-MOT-034 | Roulette Projector Sweep | Spin ambience | Projector light sweeps around the rotating wheel | Rotation-linked light frame, clamped and reduced-cost aware | Wheel rotation only | `roulette_projector_motion.dart` | `roulette_projector_motion_test.dart` |
| CIN-MOT-035 | Roulette Ticket Save | Async save | Winning film feeds and punches into a saved ticket | Feed/punch/pending/success/failure state machine | Immediate save state | `roulette_save_motion.dart` | `roulette_save_motion_test.dart` |
| CIN-MOT-036 | Roulette Suspense Hold | Reveal | Winner is concealed, teased with a clue, then revealed | Conceal/clue/hold/reveal timeline separate from wheel physics | Immediate reveal | `roulette_suspense_motion.dart` | `roulette_suspense_motion_test.dart` |
| CIN-MOT-037 | Scene Search Scanner | Search | Query scans the catalog like a cinematic frame analyzer | Focus/query-driven scanning/resolving frame; debounce remains data concern | Standard loading/result switch | `search_scanner_motion.dart` | `search_scanner_motion_test.dart` |
| CIN-MOT-038 | Similar Film Splice | Hero/navigation | Current poster splices out while similar film splices in | Source/destination handoff + custom rect tween + splice painter; nested-Hero guard | Direct replacement route | `similar_splice_motion.dart` | `similar_splice_motion_test.dart` |
| CIN-MOT-039 | Spatial Return Anchor | Reverse navigation | Returning content collapses toward the remembered source anchor | Anchor-aware collapse/reacquire frame paired with route return signal | Standard pop | `spatial_return_motion.dart` | `tile_screen_motion_test.dart` |
| CIN-MOT-040 | Stage Set Route Transition | Navigation | One tab/page exits behind a stage seam while the next enters | Route handoff + custom transition + seam occlusion; prevents simultaneous exposed pages | Fade transition | `stage_set_transition.dart` | `bottom_nav_iris_motion_test.dart` |
| CIN-MOT-041 | Subtitle Language Edit | Settings/content swap | Text exits, edit seam passes, translated text enters | Outgoing/edit/incoming frame; locale mutation occurs once under occlusion | Immediate translated text | `subtitle_language_motion.dart` | `subtitle_language_motion_test.dart` |
| CIN-MOT-042 | Synopsis Script Reveal | Content entrance | Synopsis reveals and typesets like a screenplay page | Reveal/typesetting progress frame with reverse | Final synopsis | `synopsis_script_motion.dart` | `synopsis_script_motion_test.dart` |
| CIN-MOT-043 | Living Taste Map | Data visualization | Taste signals connect and breathe as a living map | Connection/breath/drift/grain frame; weak mode removes secondary motion | Static graph | `taste_living_map_motion.dart` | `taste_living_map_motion_test.dart` |
| CIN-MOT-044 | Tile Projector Beam | Pointer/navigation | Press origin emits a projector beam that commits into navigation | Pointer-origin clamp + exposure timeline; handoff only after commit | Bounce feedback | `tile_beam_motion_timeline.dart` | `tile_beam_motion_test.dart` |
| CIN-MOT-045 | Tile-to-Screen Expansion | Hero/navigation | Dashboard tile expands into its destination and collapses back | Route-key handoff + custom rect tween + return notifier; outer Hero owns subtree | Standard route transition | `tile_screen_motion.dart` | `tile_screen_motion_test.dart` |
| CIN-MOT-046 | Watched Credits Roll | Completion | Marking watched rolls credits into a final title card | Roll/title-card frame synchronized to durable watched mutation | Immediate watched badge | `watched_credits_motion.dart` | `watched_credits_motion_test.dart` |
| CIN-MOT-047 | Watchlist Film Cut | Removal | Removed film is perforated and extracted like a strip cut | Armed perforate/extract frame with rollback reverse | Immediate removal/rollback | `watchlist_cut_motion.dart` | `watchlist_cut_motion_test.dart` |
| CIN-MOT-048 | Watchlist Stack Carry | Drag/reorder | Card lifts from a physical stack, travels, and re-registers | Drag progress + lift/carry/seat frame; bounded spread and registration | Standard reorder | `watchlist_stack_motion.dart` | `watchlist_stack_motion_test.dart` |
| CIN-MOT-049 | Weekly Plan Montage | Drag/schedule | Film scrubs through a montage into a weekly slot | Drag/lift/scrub/splice/seat frame, failure reverse | Standard drag/drop | `weekly_montage_motion.dart` | `weekly_montage_motion_test.dart` |
| CIN-MOT-050 | Weekly Ticket Flight | Schedule commit | Scheduled film becomes a ticket that flies into its day | Armed lift/flight/seat frame tied to one persistence action | Immediate scheduled card | `weekly_ticket_motion.dart` | `weekly_ticket_motion_test.dart` |

## Shared infrastructure

| ID | Name | Purpose | Source |
|---|---|---|---|
| CIN-INF-001 | Motion Runtime Profile | Central inherited runtime signal for `reducedCost`; combines device/runtime constraints without teaching individual widgets device detection | `flutterworks/kino_reforged_ios/lib/ui/animation/motion_runtime_profile.dart` |

## Integration checklist

Before adapting any entry:

- [ ] Identify the single durable user action that owns the motion.
- [ ] Write deterministic timeline boundary tests before the widget integration.
- [ ] Keep state mutation, navigation, persistence, and haptics outside `build` and outside the timeline.
- [ ] Prevent a second commit while the first is active.
- [ ] Implement failure reverse and retry focus where the action can fail.
- [ ] Implement `reduceMotion` and `weakDevice` outputs.
- [ ] Clamp all values that affect layout, clipping, paint bounds, and opacity.
- [ ] Avoid nested Hero widgets by letting an ancestor Hero own the subtree.
- [ ] Dispose controllers, focus nodes, listeners, and observers.
- [ ] Test lifecycle pause/resume and disposal during flight.
- [ ] Test compact width, large text, locale expansion, DPR, and disabled animations.
- [ ] Confirm data refresh does not replay the entrance animation.

## Contribution rules

1. IDs are append-only; never recycle or renumber an existing ID.
2. New entries require a deterministic timeline/frame test and one real widget interaction test.
3. Document reverse, cancel, retry, reduced motion, weak-device behavior, and lifecycle ownership.
4. Add the entry here before advertising it in the root indexes.
5. Keep source applications as references; promote code into `dart_files/` only after removing project-specific tokens and adding framework-level tests.
