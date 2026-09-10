---
name: NovaNodes Infrastructure Suite
colors:
  surface: '#0f131d'
  surface-dim: '#0f131d'
  surface-bright: '#353944'
  surface-container-lowest: '#0a0e18'
  surface-container-low: '#171b26'
  surface-container: '#1c1f2a'
  surface-container-high: '#262a35'
  surface-container-highest: '#313540'
  on-surface: '#dfe2f1'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dfe2f1'
  inverse-on-surface: '#2c303b'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e0fdff'
  on-primary: '#00373a'
  primary-container: '#00f2fe'
  on-primary-container: '#006a70'
  inverse-primary: '#00696f'
  secondary: '#d0bcff'
  on-secondary: '#3c0091'
  secondary-container: '#571bc1'
  on-secondary-container: '#c4abff'
  tertiary: '#e1ffec'
  on-tertiary: '#003824'
  tertiary-container: '#67f4b7'
  on-tertiary-container: '#006e4b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#0f131d'
  on-background: '#dfe2f1'
  surface-variant: '#313540'
typography:
  display-xl:
    fontFamily: Geist
    fontSize: 56px
    fontWeight: '600'
    lineHeight: 64px
    letterSpacing: -0.03em
  display-xl-mobile:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.025em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 34px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 26px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0em
  code-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: -0.01em
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0em
  telemetry-badge:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  space-2xs: 0.125rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-base: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
  space-2xl: 3rem
  space-3xl: 4rem
  gutter-mobile: 1rem
  gutter-desktop: 1.5rem
  margin-mobile: 1rem
  margin-desktop: 3rem
---

## Brand & Style

This design system expresses a high-density, mission-critical environment tailored for developers building autonomous AI agent architectures. The aesthetic merges precision minimalism with hyper-modern telemetry: dark charcoal surfaces, razor-sharp 1px structural boundaries, cosmic radial luminescence, and micro-reactive neon accents.

The emotional tone balances absolute mechanical reliability with bleeding-edge innovation. It prioritizes data density, sub-millisecond status comprehension, and visual rhythm inspired by orbital telemetry decks and contemporary high-speed developer platforms.

## Colors

The palette operates exclusively in a dark, high-contrast spectrum designed to reduce fatigue while parsing telemetry and distributed cluster states:

- **Primary (`#00f2fe` - Cyber Cyan):** Used for focus states, high-priority active links, execution triggers, and leading telemetry metrics.
- **Secondary (`#8b5cf6` - Electric Violet):** Reserved for agent node coordination, compute pipelines, machine learning models, and secondary data visualizations.
- **Tertiary (`#10b981` - Kinetic Emerald):** Dedicated strictly to operational health, live heartbeat pings, operational cluster indicators, and success confirmations.
- **Neutrals (Deep Void Series):**
  - Background Canvas: `#070913`
  - Sub-Canvas / Shell Base: `#0b0f19`
  - Structural Borders & Grids: `#1e293b` with 40-70% alpha
  - Inactive Text / Telemetry Dim: `#64748b`
  - Body Text / Neutral Bright: `#f8fafc`

## Typography

Typography enforces a strict hierarchy where structural titles rely on tight, geometric sans-serif styling (`Geist`), narrative descriptions leverage maximum neutral readability (`Inter`), and runtime outputs, keys, and statuses deploy fixed-width precision (`JetBrains Mono`).

Telemetry metrics, node addresses, latency counts, and hash strings must always use mono-spaced formatting with tabular figures to avoid layout jitter during live-stream updates.

## Layout & Spacing

This design system uses a strict 12-column fluid grid system across desktop viewports, shifting down to 6 columns on tablets and a single-column stacked layout on mobile viewports.

- **Baseline Grid:** Spacing increments adhere strictly to an 8-point system, with 4px/2px micro-steps allowed exclusively for compact telemetry tables, key-value indicators, and dense node trees.
- **Max Container Width:** 1440px for standard dashboards; edge-to-edge fluid with 24px inner rail padding for visual node canvas editors.
- **Reflow Rules:** Complex horizontal telemetry strips compress into horizontally swipeable, snapping mini-cards on mobile devices rather than wrapping into multi-line tables.

## Elevation & Depth

Visual depth is achieved through translucent glass planes, directional inner borders, and focused cosmic radiance rather than heavy drop shadows:

- **Surface Layer 0 (Canvas):** Pure void `#070913` with subtle background linear grid patterns (1px grid lines at 4% opacity).
- **Surface Layer 1 (Base Cards):** `#0b0f19` at 85% opacity with `backdrop-filter: blur(12px)` and a 1px border colored `rgba(255, 255, 255, 0.08)`.
- **Surface Layer 2 (Raised Modals & Popovers):** `#131929` at 92% opacity with `backdrop-filter: blur(20px)`, top-edge highlight (`linear-gradient(90deg, transparent, rgba(0, 242, 254, 0.25), transparent)`), and ambient shadow `0 20px 40px -15px rgba(0, 0, 0, 0.7)`.
- **Radial Lighting:** Cards on hover trigger a localized radial lighting effect: `radial-gradient(400px circle at var(--mouse-x) var(--mouse-y), rgba(0, 242, 254, 0.06), transparent 80%)`.

## Shapes

The system relies on compact, disciplined roundedness (`roundedness: 1`). Corner radii are deliberately restrained to reinforce an engineering-grade, surgical feel:

- **Micro elements (Badges, Pills, Buttons, Inputs):** 4px to 6px border radius.
- **Cards, Panels, Modals:** 8px (`rounded-lg`).
- **Pills / Status Dots:** Fully rounded (9999px) strictly for status indicators and micro status chips.

## Components

### Buttons
- **Primary:** Neon Cyan background (`#00f2fe`) with crisp dark typography (`#070913`), semi-bold weight. Hover state triggers an expanded 12px outer glow (`box-shadow: 0 0 16px rgba(0, 242, 254, 0.35)`).
- **Secondary:** Surface charcoal (`#131929`), 1px border (`rgba(255, 255, 255, 0.12)`), text `#f8fafc`. Hover transitions border to `#8b5cf6` with text color shift.
- **Ghost/Tertiary:** Transparent fill with muted text (`#64748b`), converting to text `#00f2fe` on hover.

### Telemetry Badges & Chips
- Embedded monospace typography (`JetBrains Mono`, 11px).
- Translucent dark fills with 10% opacity colored backgrounds matched to their operational states (e.g., cyan for agent coordination, emerald for online nodes, violet for heavy compute).
- Outer border matched at 30% border opacity.

### Online Status Indicators (Pings)
- Double-element construct: an inner solid 6px dot (`#10b981`) paired with an outer 14px concentric ping ring executing an infinite CSS radar ping animation (`scale(1.8)`, opacity fading to 0).

### Inputs & Terminal Console Fields
- Monospaced inputs for execution triggers and configurations.
- Dark hollow background (`#0b0f19`), inset 1px border (`rgba(255, 255, 255, 0.1)`).
- Focus state switches border to `#00f2fe` with an inner 2px shadow ring of `rgba(0, 242, 254, 0.2)`.

### Glass Cards & Node Blocks
- Multi-tier glass cards with inset top highlight border line (`1px solid rgba(255, 255, 255, 0.08)`).
- Headers clearly separated by a hairline divider with mono labels and secondary status action buttons.
- Node block connectors highlight with dynamic gradient pulses (`#00f2fe` to `#8b5cf6`) when active pipeline executions run.
