import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE } from '../tokens/layout';

/**
 * Ch1Chrome — the shared chassis for the INFO 7375 Chapter 1 reel
 * ("The Token That Followed", persona Sasha).
 *
 * Every Ch1Pretrain* scene renders INSIDE <Ch1Stage>, so the reel's frame
 * furniture is defined exactly once:
 *
 *   - the claude illustration ground (#F2F0E9) — fidelity palette, not retinted
 *   - SPARK-LINE LAW: one short serif line per beat, top by default,
 *     bottom when the illustration owns the top of the frame
 *   - the ACADEMIC HONESTY banner ("CONSTRUCTED EXAMPLE") — this reel's
 *     numbers are invented teaching values, and the frame says so out loud
 *     on every beat that shows one
 *   - LOGO LAW: a small low-opacity course bug, lower-right, inside SAFE
 *
 * All furniture sits inside the shared SAFE inset (x 96–1824, y 54–1026) and
 * is positioned FROM SAFE, never nudged by pixels. Scenes get the interior.
 *
 * Channel note: this reel is `claude-sasha` (a course channel), not
 * claude-liam, so it does NOT use ClaudeTitleOutro — that component hardcodes
 * @NikBearBrown and OUTRO-LOCK.md scopes it to claude-liam reels only.
 * Ch1PretrainOutro is this channel's own title-restate card.
 */

// ── Palette (inherited, never retinted) ─────────────────────────────────────

export const CH1 = {
  /** The claude illustration stage — slightly deeper than the app's page cream. */
  GROUND: '#F2F0E9',
  INK: CLAUDE.INK,
  INK_SOFT: CLAUDE.INK_SOFT,
  /** THE one accent per beat. */
  SPARK: CLAUDE.SPARK,
  /** Deeper accent step — used ONLY for the struck/zeroed state. */
  WARN: '#A44A32',
  CARD: '#FFFFFF',
  BORDER: '#DCD8CB',
  /** Legibility floor: un-highlighted elements never fade below this. */
  DIM: 0.45,
} as const;

export const SERIF = CLAUDE_FONT.serif;
export const SANS = CLAUDE_FONT.ui;
export const MONO = CLAUDE_FONT.mono;

// ── Timing helpers (pure functions of progress) ─────────────────────────────

export const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

/** Map x from [x0,x1] onto [y0,y1], clamped at both ends. */
export const remap = (x: number, x0: number, x1: number, y0: number, y1: number) =>
  y0 + (y1 - y0) * clamp((x - x0) / (x1 - x0 || 1), 0, 1);

/** Cubic ease-out — the house curve for reveals. */
export const ease = (t: number) => 1 - Math.pow(1 - clamp(t, 0, 1), 3);

/** A reveal that lands ON the spoken word: 0 before `from`, 1 after `to`. */
export const cue = (p: number, from: number, to: number) => ease(remap(p, from, to, 0, 1));

/**
 * Normalized beat progress in [0,1].
 *
 * Every Ch1 scene is a pure function of this, so a beat re-renders identically
 * at any duration — which matters because compile.py conforms each scene to
 * the MEASURED audio length, not to a frame count guessed at authoring time.
 */
export const useBeatProgress = (): number => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
};

// ── The spark line ──────────────────────────────────────────────────────────

const SparkGlyph: React.FC<{ size: number; opacity: number }> = ({ size, opacity }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{ opacity, flexShrink: 0 }}>
    {/* The Claude spark — four-point star, terracotta, the one accent. */}
    <path
      d="M12 1.6 L13.9 9.4 L21.2 12 L13.9 14.6 L12 22.4 L10.1 14.6 L2.8 12 L10.1 9.4 Z"
      fill={CH1.SPARK}
    />
  </svg>
);

// ── The stage ───────────────────────────────────────────────────────────────

export type Ch1StageProps = {
  /** SPARK-LINE LAW: one short serif line, <= ~5 words. Empty = spark alone. */
  sparkLine?: string;
  /** Where the line sits. 'bottom' when the illustration owns the top. */
  sparkPos?: 'top' | 'bottom';
  /** Academic-honesty banner, top-right. '' = no banner. */
  banner?: string;
  /** LOGO LAW bug, lower-right. */
  chip?: string;
  children?: React.ReactNode;
};

export const Ch1Stage: React.FC<Ch1StageProps> = ({
  sparkLine = '',
  sparkPos = 'top',
  banner = 'CONSTRUCTED EXAMPLE',
  chip = 'INFO 7375 · CH 1',
  children,
}) => {
  const p = useBeatProgress();

  // Furniture fades in first so the interior never pops in over a bare ground.
  const sparkO = cue(p, 0.02, 0.10);
  const bannerO = cue(p, 0.04, 0.14);
  const chipO = cue(p, 0.06, 0.16);

  const SPARK_BAND = 84;   // reserved furniture band, measured from SAFE
  const CHIP_BAND = 46;

  return (
    <AbsoluteFill style={{ background: CH1.GROUND }}>
      {/* ── SPARK-LINE LAW ── */}
      {sparkLine ? (
        <div
          style={{
            position: 'absolute',
            left: SAFE.x,
            width: SAFE.w,
            ...(sparkPos === 'top'
              ? { top: SAFE.y }
              : { top: SAFE.b - SPARK_BAND }),
            height: SPARK_BAND,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 18,
            opacity: sparkO,
          }}
        >
          <SparkGlyph size={38} opacity={1} />
          <div
            style={{
              fontFamily: SERIF,
              fontSize: 46,
              fontWeight: 600,
              color: CH1.INK,
              letterSpacing: '-0.01em',
              maxWidth: SAFE.w - 120,
              overflow: 'hidden',
              textOverflow: 'ellipsis',
              whiteSpace: 'nowrap',
            }}
          >
            {sparkLine}
          </div>
        </div>
      ) : null}

      {/* ── ACADEMIC HONESTY banner ── */}
      {banner ? (
        <div
          style={{
            position: 'absolute',
            top: SAFE.y + 6,
            right: SAFE.x,
            fontFamily: SANS,
            fontSize: 20,
            fontWeight: 800,
            letterSpacing: '0.14em',
            color: CH1.WARN,
            background: CH1.GROUND,
            border: `2px solid ${CH1.WARN}`,
            borderRadius: 5,
            padding: '7px 14px',
            lineHeight: 1,
            opacity: bannerO * 0.92,
          }}
        >
          {banner}
        </div>
      ) : null}

      {/* ── the interior: everything inside SAFE, minus the furniture bands ── */}
      <div
        style={{
          position: 'absolute',
          left: SAFE.x,
          width: SAFE.w,
          top: SAFE.y + (sparkPos === 'top' && sparkLine ? SPARK_BAND : 0),
          height:
            SAFE.h -
            (sparkLine ? SPARK_BAND : 0) -
            CHIP_BAND,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
        }}
      >
        {children}
      </div>

      {/* ── LOGO LAW bug: small, low-opacity, lower-right, inside SAFE ── */}
      <div
        style={{
          position: 'absolute',
          bottom: 1080 - SAFE.b,
          right: SAFE.x,
          display: 'flex',
          alignItems: 'center',
          gap: 10,
          opacity: chipO * 0.5,
        }}
      >
        <SparkGlyph size={19} opacity={1} />
        <span
          style={{
            fontFamily: SANS,
            fontSize: 20,
            fontWeight: 700,
            letterSpacing: '0.1em',
            color: CH1.INK,
          }}
        >
          {chip}
        </span>
      </div>
    </AbsoluteFill>
  );
};

// ── Shared primitives ───────────────────────────────────────────────────────

/** A tokenized word chip — the reel's atomic unit. */
export const Ch1Token: React.FC<{
  text: string;
  state?: 'rest' | 'focus' | 'slot' | 'struck';
  opacity?: number;
  fontSize?: number;
}> = ({ text, state = 'rest', opacity = 1, fontSize = 48 }) => {
  const focus = state === 'focus';
  const slot = state === 'slot';
  const struck = state === 'struck';
  return (
    <span
      style={{
        fontFamily: MONO,
        fontSize,
        fontWeight: focus || slot ? 700 : 500,
        color: struck ? CH1.WARN : focus || slot ? CH1.CARD : CH1.INK,
        background: focus ? CH1.SPARK : slot ? CH1.INK : 'transparent',
        border: slot ? `3px dashed ${CH1.SPARK}` : `3px solid transparent`,
        borderRadius: 8,
        padding: '10px 16px',
        textDecoration: struck ? 'line-through' : 'none',
        opacity,
        lineHeight: 1.1,
        whiteSpace: 'nowrap',
      }}
    >
      {text}
    </span>
  );
};

/** A labelled horizontal bar. `frac` is already eased by the caller. */
export const Ch1Bar: React.FC<{
  frac: number;
  width: number;
  height?: number;
  accent?: boolean;
  dim?: boolean;
}> = ({ frac, width, height = 40, accent = false, dim = false }) => (
  <div
    style={{
      width,
      height,
      background: '#E4E0D4',
      borderRadius: 4,
      overflow: 'hidden',
      opacity: dim ? CH1.DIM + 0.25 : 1,
    }}
  >
    <div
      style={{
        width: `${clamp(frac, 0, 1) * 100}%`,
        height: '100%',
        background: accent ? CH1.SPARK : CH1.INK,
        borderRadius: 4,
      }}
    />
  </div>
);
