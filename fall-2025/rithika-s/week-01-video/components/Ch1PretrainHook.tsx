import React from 'react';
import { z } from 'zod';
import { Ch1Stage, CH1, SERIF, SANS, MONO, cue, clamp, useBeatProgress } from './Ch1Chrome';

/**
 * Ch1PretrainHook — Act 1. The cold open, with no math anywhere on screen.
 *
 * The reel opens on the false claim as a plain English sentence, because a
 * viewer who has never heard of next-token prediction has nothing to hang a
 * logit on yet. First the sentence. Then the question. Then a genuine pause
 * in which the viewer answers it themselves — the beat's audio carries
 * trailing silence for exactly that purpose, so the hold is real and not an
 * illusion of one.
 *
 * The answer is deliberately NOT shown here. 'green' lights and the next slot
 * opens as a question mark, and that is where the beat ends.
 */

export const ch1PretrainHookSchema = z.object({
  /**
   * Beat length in seconds, from the MEASURED audio (including the appended
   * guess-pause silence). calculateMetadata turns it into the frame count.
   */
  durationS: z.number().default(15),
  line: z.string().default('The moon is made of green cheese.'),
  /** The conditioning word the question asks about. */
  focusWord: z.string().default('green'),
  question: z.string().default(
    'If a model reads this sentence, what does it learn to predict comes after “green”?',
  ),
  /** Shown during the pause, while the viewer answers for themselves. */
  pausePrompt: z.string().default('Your guess first.'),
  sparkLine: z.string().default('One sentence.'),
});
export type Ch1PretrainHookProps = z.infer<typeof ch1PretrainHookSchema>;

export const Ch1PretrainHook: React.FC<Ch1PretrainHookProps> = (props) => {
  const p = useBeatProgress();
  const { line, focusWord, question, pausePrompt, sparkLine } =
    ch1PretrainHookSchema.parse(props);

  // ── Timeline: sentence → question → the pause ──
  const lineO = cue(p, 0.02, 0.16);
  const focusO = cue(p, 0.30, 0.40);      // 'green' takes the accent
  const qO = cue(p, 0.34, 0.50);
  const slotO = cue(p, 0.56, 0.66);       // the dashed slot opens
  const pauseO = cue(p, 0.70, 0.80);

  // The caret pulses through the pause so the hold reads as deliberate.
  const pulse = 0.55 + 0.45 * Math.sin(p * 46);

  const words = line.replace(/\.$/, '').split(/\s+/);
  const stop = line.trim().endsWith('.');

  return (
    <Ch1Stage sparkLine={sparkLine} sparkPos="top" banner="CONSTRUCTED EXAMPLE">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 54, justifyContent: 'center' }}>
        {/* ── the claim, as plain English ── */}
        <div
          style={{
            fontFamily: SERIF,
            fontSize: 92,
            fontWeight: 600,
            color: CH1.INK,
            letterSpacing: '-0.02em',
            lineHeight: 1.16,
            opacity: lineO,
            display: 'flex',
            flexWrap: 'wrap',
            gap: '0 24px',
            alignItems: 'baseline',
          }}
        >
          {words.map((w, i) => {
            const isFocus = w.toLowerCase() === focusWord.toLowerCase();
            const isLast = i === words.length - 1;
            return (
              <span
                key={i}
                style={{
                  color: isFocus ? CH1.SPARK : CH1.INK,
                  fontWeight: isFocus ? 700 : 600,
                  // the focus word lifts out of the sentence as the question lands
                  opacity: isFocus ? 0.55 + 0.45 * focusO : 1,
                }}
              >
                {w}
                {isLast && stop ? <span style={{ color: CH1.INK }}>.</span> : null}
              </span>
            );
          })}
        </div>

        {/* ── the question, asked before any mechanism ── */}
        <div
          style={{
            opacity: qO,
            borderLeft: `6px solid ${CH1.SPARK}`,
            paddingLeft: 32,
            display: 'flex',
            flexDirection: 'column',
            gap: 26,
          }}
        >
          <div style={{ fontFamily: SANS, fontSize: 44, color: CH1.INK, lineHeight: 1.34, fontWeight: 600, maxWidth: 1560 }}>
            {question}
          </div>

          {/* the slot the question is about, opened but not answered */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 20, opacity: slotO }}>
            <span style={{ fontFamily: MONO, fontSize: 46, color: CH1.INK_SOFT }}>
              … of
            </span>
            <span style={{ fontFamily: MONO, fontSize: 46, fontWeight: 700, color: CH1.CARD, background: CH1.SPARK, padding: '10px 18px', borderRadius: 8 }}>
              {focusWord}
            </span>
            <span
              style={{
                fontFamily: MONO,
                fontSize: 46,
                fontWeight: 800,
                color: CH1.INK,
                background: CH1.CARD,
                border: `3px dashed ${CH1.SPARK}`,
                borderRadius: 8,
                padding: '10px 26px',
                opacity: clamp(pulse, 0, 1),
              }}
            >
              ?
            </span>
          </div>
        </div>

        {/* ── the pause ── */}
        <div
          style={{
            opacity: pauseO,
            fontFamily: SANS,
            fontSize: 32,
            fontWeight: 700,
            letterSpacing: '0.1em',
            textTransform: 'uppercase' as const,
            color: CH1.SPARK,
          }}
        >
          {pausePrompt}
        </div>
      </div>
    </Ch1Stage>
  );
};

export const ch1PretrainHookDemoDefaultProps: Ch1PretrainHookProps =
  ch1PretrainHookSchema.parse({});
