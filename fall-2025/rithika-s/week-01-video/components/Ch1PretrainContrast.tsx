import React from 'react';
import { z } from 'zod';
import { Ch1Stage, CH1, SERIF, SANS, MONO, cue, useBeatProgress } from './Ch1Chrome';

/**
 * Ch1PretrainContrast — Act 3. The beat that turns "not the truth" from an
 * assertion into a mechanism.
 *
 * Same model, same four logits, same forward pass. The ONLY thing that
 * changes between the two columns is which sentence sat in the corpus — and
 * the target vector flips with it. That is the whole argument: if the target
 * were built from truth, the left and right columns would be identical. They
 * are not, because the target is read off the text.
 *
 * Both target vectors are emitted and asserted by verify_softmax.py
 * (`y_false`, `y_true`), so neither column is hand-typed.
 */

export const ch1PretrainContrastSchema = z.object({
  durationS: z.number().default(28),
  sparkLine: z.string().default('Change the text, change the target.'),
  vocab: z.array(z.string()).default(['rock', 'cheese', 'gas', 'light']),
  falseLine: z.string().default('The moon is made of green cheese'),
  trueLine: z.string().default('The moon is made of grey rock'),
  /** One-hot target when the corpus holds the FALSE sentence. */
  yFalse: z.array(z.number()).default([0, 1, 0, 0]),
  /** One-hot target when the corpus holds the TRUE sentence. */
  yTrue: z.array(z.number()).default([1, 0, 0, 0]),
  falseTarget: z.string().default('cheese'),
  trueTarget: z.string().default('rock'),
  closing: z.string().default(
    'Identical weights. Identical scores. Only the sentence changed — and the target moved with it.',
  ),
});
export type Ch1PretrainContrastProps = z.infer<typeof ch1PretrainContrastSchema>;

const Column: React.FC<{
  eyebrow: string;
  line: string;
  vocab: string[];
  y: number[];
  hot: string;
  accent: boolean;
  reveal: (i: number) => number;
  headO: number;
}> = ({ eyebrow, line, vocab, y, hot, accent, reveal, headO }) => {
  const words = line.split(/\s+/);
  const last = words.length - 1;
  return (
    <div
      style={{
        flex: 1,
        border: `4px solid ${accent ? CH1.SPARK : CH1.INK_SOFT}`,
        borderRadius: 14,
        padding: '28px 32px 32px',
        background: accent ? 'rgba(217,119,87,0.06)' : 'rgba(61,57,41,0.035)',
        display: 'flex',
        flexDirection: 'column',
        gap: 18,
        opacity: headO,
      }}
    >
      <div style={{ fontFamily: SANS, fontSize: 21, fontWeight: 800, letterSpacing: '0.13em', color: accent ? CH1.SPARK : CH1.INK_SOFT }}>
        {eyebrow}
      </div>

      {/* the corpus line, with its final token marked as the one that followed */}
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0 10px', alignItems: 'baseline' }}>
        {words.map((w, i) => (
          <span
            key={i}
            style={{
              fontFamily: MONO,
              fontSize: 33,
              fontWeight: i === last ? 700 : 500,
              color: i === last ? (accent ? CH1.SPARK : CH1.INK) : CH1.INK_SOFT,
              textDecoration: i === last ? 'underline' : 'none',
              textUnderlineOffset: 6,
            }}
          >
            {w}
          </span>
        ))}
      </div>

      <div style={{ fontFamily: SANS, fontSize: 20, fontWeight: 800, letterSpacing: '0.12em', color: CH1.INK_SOFT, marginTop: 6 }}>
        TARGET VECTOR y
      </div>

      {/* the one-hot vector that this corpus produces */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 11 }}>
        {vocab.map((t, i) => {
          const isHot = y[i] === 1;
          return (
            <div key={t} style={{ display: 'flex', alignItems: 'center', gap: 18, opacity: reveal(i) }}>
              <div
                style={{
                  width: 210,
                  fontFamily: MONO,
                  fontSize: 34,
                  fontWeight: isHot ? 700 : 500,
                  color: isHot ? (accent ? CH1.SPARK : CH1.INK) : CH1.INK_SOFT,
                }}
              >
                {t}
              </div>
              <div
                style={{
                  width: 66,
                  height: 66,
                  borderRadius: 9,
                  border: `4px solid ${isHot ? (accent ? CH1.SPARK : CH1.INK) : CH1.BORDER}`,
                  background: isHot ? (accent ? CH1.SPARK : CH1.INK) : CH1.CARD,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontFamily: MONO,
                  fontSize: 36,
                  fontWeight: 800,
                  color: isHot ? CH1.CARD : CH1.INK_SOFT,
                }}
              >
                {y[i]}
              </div>
              {isHot ? (
                <span style={{ fontFamily: SANS, fontSize: 21, fontWeight: 700, color: accent ? CH1.SPARK : CH1.INK_SOFT, whiteSpace: 'nowrap' }}>
                  ← {hot}
                </span>
              ) : null}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export const Ch1PretrainContrast: React.FC<Ch1PretrainContrastProps> = (props) => {
  const p = useBeatProgress();
  const {
    sparkLine, vocab, falseLine, trueLine, yFalse, yTrue,
    falseTarget, trueTarget, closing,
  } = ch1PretrainContrastSchema.parse(props);

  const leftO = cue(p, 0.03, 0.14);
  const leftRow = (i: number) => cue(p, 0.14 + i * 0.035, 0.24 + i * 0.035);
  const rightO = cue(p, 0.40, 0.52);
  const rightRow = (i: number) => cue(p, 0.46 + i * 0.035, 0.56 + i * 0.035);
  const closeO = cue(p, 0.78, 0.90);

  return (
    <Ch1Stage sparkLine={sparkLine} sparkPos="top" banner="CONSTRUCTED EXAMPLE">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 26 }}>
        <div style={{ display: 'flex', gap: 40, alignItems: 'stretch' }}>
          <Column
            eyebrow="THE CORPUS WE HAVE"
            line={falseLine}
            vocab={vocab}
            y={yFalse}
            hot={`“${falseTarget}” followed`}
            accent
            reveal={leftRow}
            headO={leftO}
          />
          <Column
            eyebrow="IF THE CORPUS SAID THE TRUE THING"
            line={trueLine}
            vocab={vocab}
            y={yTrue}
            hot={`“${trueTarget}” followed`}
            accent={false}
            reveal={rightRow}
            headO={rightO}
          />
        </div>

        <div
          style={{
            opacity: closeO,
            borderTop: `3px solid ${CH1.INK}`,
            paddingTop: 18,
            fontFamily: SERIF,
            fontSize: 38,
            fontWeight: 600,
            color: CH1.INK,
            lineHeight: 1.3,
          }}
        >
          {closing}
        </div>
      </div>
    </Ch1Stage>
  );
};

export const ch1PretrainContrastDemoDefaultProps: Ch1PretrainContrastProps =
  ch1PretrainContrastSchema.parse({});
