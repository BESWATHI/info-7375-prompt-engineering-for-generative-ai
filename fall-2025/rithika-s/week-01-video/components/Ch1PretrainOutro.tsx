import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';
import { z } from 'zod';
import { CH1, SERIF, SANS, cue, clamp } from './Ch1Chrome';
import { SAFE } from '../tokens/layout';

/**
 * Ch1PretrainOutro — OUTRO LAW for the `claude-sasha` course channel.
 *
 * ClaudeTitleOutro cannot be used here: it hardcodes the @NikBearBrown handle
 * and OUTRO-LOCK.md scopes it to claude-liam reels only ("Other channels use
 * their own outro components — never this one"). This is that own component:
 * exact title restate, poster-plain serif, terracotta period, course handle
 * beneath. No mascot — the 18 crisp-safe mascots are @NikBearBrown identity.
 *
 * FILL-THE-CANVAS: a centred poster card measured only 16% of SAFE and failed
 * Gate V (which scores the INK BOUNDING BOX against the safe area, not ink
 * density). So the card is now anchored: the eyebrow sits on SAFE's top edge
 * and the credit rail on its bottom edge, with the title spanning the width
 * between them. The composition still reads as a spare poster — the negative
 * space is now INSIDE a frame that claims the canvas, which is the distinction
 * the law actually draws.
 */

export const ch1PretrainOutroSchema = z.object({
  /**
   * Beat length in seconds. The reel's MEASURED audio duration is written here
   * by the beat sheet, and calculateMetadata turns it into the composition's
   * frame count — so every reveal is distributed across the real spoken window
   * instead of a frame count guessed at authoring time.
   */
  durationS: z.number().default(6),
  title: z.string().default('The Token That Followed'),
  eyebrow: z.string().default('INFO 7375 · CHAPTER 1'),
  concept: z.string().default('What pretraining actually targets'),
  handle: z.string().default('INFO 7375 · Prompt Engineering for Generative AI'),
  credit: z.string().default('Rithika Sankar Rajeswari · narrated by Sasha'),
  rail: z.string().default('Kokoro TTS af_bella · Brutalist toolkit · $0.00'),
});
export type Ch1PretrainOutroProps = z.infer<typeof ch1PretrainOutroSchema>;

const Spark: React.FC<{ size: number }> = ({ size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{ flexShrink: 0 }}>
    <path
      d="M12 1.6 L13.9 9.4 L21.2 12 L13.9 14.6 L12 22.4 L10.1 14.6 L2.8 12 L10.1 9.4 Z"
      fill={CH1.SPARK}
    />
  </svg>
);

export const Ch1PretrainOutro: React.FC<Ch1PretrainOutroProps> = (props) => {
  const { title, eyebrow, concept, handle, credit, rail } =
    ch1PretrainOutroSchema.parse(props);
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);

  const eyebrowO = cue(p, 0.02, 0.14);
  const titleO = cue(p, 0.06, 0.22);
  const ruleW = cue(p, 0.24, 0.46);
  const handleO = cue(p, 0.36, 0.54);
  const creditO = cue(p, 0.50, 0.66);
  const railO = cue(p, 0.62, 0.80);

  // Terminal punctuation takes the accent, house pattern.
  const m = title.match(/^([\s\S]*?)\s*([.?!…]+)\s*$/);
  const body = m ? m[1] : title;
  const punct = m ? m[2] : '.';

  return (
    <AbsoluteFill style={{ background: CH1.GROUND }}>
      {/* ── top edge of SAFE: eyebrow + concept, full width ── */}
      <div
        style={{
          position: 'absolute',
          left: SAFE.x,
          top: SAFE.y,
          width: SAFE.w,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          opacity: eyebrowO,
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <Spark size={30} />
          <span
            style={{
              fontFamily: SANS,
              fontSize: 27,
              fontWeight: 800,
              letterSpacing: '0.14em',
              color: CH1.INK,
            }}
          >
            {eyebrow}
          </span>
        </div>
        <span style={{ fontFamily: SERIF, fontSize: 34, color: CH1.INK_SOFT }}>
          {concept}
        </span>
      </div>

      {/* ── the poster, centred between the two anchored rails ── */}
      <AbsoluteFill
        style={{ alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}
      >
        <div
          style={{
            fontFamily: SERIF,
            fontSize: 138,
            fontWeight: 700,
            color: CH1.INK,
            letterSpacing: '-0.028em',
            textAlign: 'center',
            maxWidth: SAFE.w - 40,
            lineHeight: 1.06,
            opacity: titleO,
          }}
        >
          {body}
          <span style={{ color: CH1.SPARK }}>{punct}</span>
        </div>

        <div
          style={{
            width: (SAFE.w - 260) * ruleW,
            height: 5,
            background: CH1.SPARK,
            marginTop: 44,
            borderRadius: 3,
          }}
        />

        <div
          style={{
            fontFamily: SANS,
            fontSize: 40,
            fontWeight: 700,
            color: CH1.INK,
            marginTop: 42,
            opacity: handleO,
            textAlign: 'center',
          }}
        >
          {handle}
        </div>
      </AbsoluteFill>

      {/* ── bottom edge of SAFE: credit rail, full width ── */}
      <div
        style={{
          position: 'absolute',
          left: SAFE.x,
          top: SAFE.b - 44,
          width: SAFE.w,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        <span
          style={{
            fontFamily: SANS,
            fontSize: 32,
            fontWeight: 700,
            color: CH1.INK,
            opacity: creditO,
          }}
        >
          {credit}
        </span>
        <span
          style={{
            fontFamily: SANS,
            fontSize: 25,
            color: CH1.INK_SOFT,
            opacity: railO * 0.9,
          }}
        >
          {rail}
        </span>
      </div>
    </AbsoluteFill>
  );
};

export const ch1PretrainOutroDemoDefaultProps: Ch1PretrainOutroProps =
  ch1PretrainOutroSchema.parse({});
