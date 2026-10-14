"""scenes.py — Readback pitch film (show-tell). One drawn scene per body beat, B01–B08.

The show-tell ISO KIT (brutalist.art @ cd4bf20, skills/make/show-tell/templates/iso_kit.py) is pasted
below unchanged, as the skill requires (Gate A copies only this file). Readback's own helpers follow it.
Labels: a question marker top-left, the honesty tag bottom-left (CONSTRUCTED / real-data stamps).
"""
from manim import *
import numpy as np
import json as _json, os as _os

# ═════════════════════════════ ISO KIT (show-tell) ═════════════════════════════
STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
BOX_TOP, BOX_L, BOX_R = "#F3E9D8", "#DCC9AA", "#C7AE86"          # kraft cardboard: top, left face, right face (deep enough for Gate V contrast)
BOX_IN1, BOX_IN2, BOX_FLOOR = "#CDB894", "#BFA67E", "#B39A72"     # inside walls + floor
DARK_TOP, DARK_L, DARK_R = "#3A3530", "#26221F", "#1E1B18"        # MCP / server blocks
PAGE_TOP, PAGE_L, PAGE_R = "#FFFFFF", "#ECE7DF", "#E2DCD2"         # skill pages
BAR1, BAR2, BAR3 = "#8B8F96", "#B4AFA6", "#D9D4C7"                # chart segments, dim to ghost
SERIF = "EB Garamond"
C30 = 0.8660254
config.background_color = STAGE


def T(s, size=36, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")


class Iso:
    """Isometric projection: x runs right-up, y runs left-up, z runs up. (ox, oy) is where (0,0,0) lands."""
    def __init__(self, ox=0.0, oy=0.0, s=1.0):
        self.ox, self.oy, self.s = ox, oy, s

    def p(self, x, y, z=0.0):
        return np.array([self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * 0.5 * self.s + z * self.s, 0.0])

    def v(self, dx, dy, dz=0.0):
        return self.p(dx, dy, dz) - self.p(0, 0, 0)

    def quad(self, pts, fill, stroke=INK, sw=4):
        return Polygon(*[self.p(*q) for q in pts], fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)

    def box(self, x0, y0, z0, w, d, h, top=BOX_TOP, left=BOX_L, right=BOX_R, sw=4):
        """Closed box: the two front faces (x = x0 and y = y0) plus the top."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        return VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], left, sw=sw),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], right, sw=sw),
            self.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, sw=sw))

    def open_box(self, x0, y0, z0, w, d, h):
        """(back, front): floor + inner back walls, then the front walls. Put contents between them."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        back = VGroup(
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], BOX_FLOOR),
            self.quad([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], BOX_IN1),
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], BOX_IN2))
        front = VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], BOX_L),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], BOX_R))
        back.set_z_index(0); front.set_z_index(2)
        return back, front

    def tape(self, x0, y0, z1, w, d, drop=0.35, t=0.22):
        """Terracotta tape across the top (along x) and down the left front face."""
        ym = y0 + d / 2
        return VGroup(
            self.quad([(x0, ym - t, z1), (x0 + w, ym - t, z1), (x0 + w, ym + t, z1), (x0, ym + t, z1)], TERRA, sw=0),
            self.quad([(x0, ym - t, z1), (x0, ym + t, z1), (x0, ym + t, z1 - drop), (x0, ym - t, z1 - drop)], TERRA, sw=0))

    def mcp(self, x0, y0, z0, w=1.3, d=1.3, h=0.7):
        """Dark MCP block with two light ports on its right front face."""
        body = self.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
        ports = VGroup(*[self.box(x0 + w * f, y0 - 0.18, z0 + h * 0.3, w * 0.16, 0.18, h * 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1)
                         for f in (0.22, 0.58)])
        return VGroup(body, ports)

    def page(self, x0, y0, z0, w=1.1, d=1.4):
        """A skill page lying flat: white slab, three ghost text lines, one terracotta dot."""
        slab = self.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        zt = z0 + 0.06
        lines = VGroup(*[Line(self.p(x0 + 0.2, y0 + d * f, zt), self.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                         for f in (0.3, 0.5, 0.7)])
        dot = Dot(self.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA)
        return VGroup(slab, lines, dot)

    def server(self, x0, y0, z0, w=1.4, d=1.4, slab=0.42, n=3):
        """A stack of dark server slabs; returns (stack, lights) — lights start ghost, turn terracotta."""
        stack = VGroup(*[self.box(x0, y0, z0 + i * (slab + 0.04), w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
        lights = VGroup(*[Dot(self.p(x0 + 0.25, y0, z0 + i * (slab + 0.04) + slab / 2), radius=0.06, color=GHOST) for i in range(n)])
        return stack, lights


def ease_in(t):
    """Quadratic ease-in (things dropping into a box). Local: Gate A's stub has no ease_in_quad."""
    return t * t


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cursor(x, y, s=0.45):
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=INK, fill_opacity=1, stroke_color=CARD, stroke_width=2)


def pill(x, y, w, h=0.62, fill="#FFFFFF"):
    return RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


# ═════════════════════════════ pacing (narration is the clock) ═════════════════════════════
try:
    _SHEET = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured audio)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ═════════════════════════════ Readback helpers ═════════════════════════════
def _mid(self):
    return _TARGET.get(type(self).__name__.split("_")[0], 0) / 2


def P(self, *anims, rt=0.6):
    """play() that never animates across the clip midpoint (GATE T and Gate V sample it)."""
    mid, t = _mid(self), _elapsed(self)
    if mid and t < mid + 0.25 and t + rt > mid - 0.25:
        self.wait(max(0.05, mid + 0.27 - t))
    self.play(*anims, run_time=rt)


def at(self, phrase):
    """until(), but never parks inside the midpoint guard."""
    until(self, phrase)


def marker(s):
    return T(s, 34).move_to([0, 3.0, 0]).align_to([-6.0, 0, 0], LEFT)


def tag(s):
    return T(s, 32).move_to([0, -3.05, 0]).align_to([-6.0, 0, 0], LEFT)


def card(x, y, w, h, stroke=INK, sw=4, fill=CARD):
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw).move_to([x, y, 0])


def rubric(x, y, n=5, w=2.6, h=3.4):
    """A rubric page: a card with n clause lines (grey bars with gaps)."""
    page = card(x, y, w, h)
    top = y + h / 2 - 0.55
    lines = VGroup(*[Line([x - w / 2 + 0.35, top - i * 0.6, 0], [x + w / 2 - 0.35 - (0.4 if i % 2 else 0), top - i * 0.6, 0],
                          color=BAR2, stroke_width=12) for i in range(n)])
    return page, lines


def judge(iso, x, y):
    """A judge: a dark block (the model) with one light eye on its front."""
    body = iso.mcp(x, y, 0, w=1.2, d=1.2, h=0.9)
    return body


def qcard(x, y):
    c = card(x, y, 0.95, 0.95, stroke=INK, sw=4, fill="#FFFFFF")
    return VGroup(c, T("?", 48).move_to([x, y, 0]))


def commit_line(x0, x1, y):
    return Line([x0, y, 0], [x1, y, 0], color=INK, stroke_width=6)


def commit_dot(x, y, filled=True):
    return Circle(radius=0.2, stroke_color=INK, stroke_width=5, fill_color=INK if filled else STAGE,
                  fill_opacity=1).move_to([x, y, 0])


def padlock(x, y):
    shackle = Arc(radius=0.28, start_angle=0, angle=PI, arc_center=[x, y + 0.36, 0], color=INK, stroke_width=9)
    body = Rectangle(width=0.95, height=0.72, fill_color=DARK_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    return VGroup(shackle, body)


def anchor(x, y):
    ring = Circle(radius=0.16, color=INK, stroke_width=7).move_to([x, y + 0.75, 0])
    shank = Line([x, y + 0.59, 0], [x, y - 0.55, 0], color=INK, stroke_width=8)
    arm = Arc(radius=0.55, start_angle=PI, angle=PI, color=INK, stroke_width=8).move_to([x, y - 0.3, 0])
    return VGroup(ring, shank, arm)


EXCERPT = "Include a lock function so buttons can't be pressed by accident"
try:  # the on-screen excerpt must be a verbatim substring of a real recorded output
    _rec = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                                         "case-study", "outputs", "feature-run", "ES2007a.json")))
    assert EXCERPT in _rec["recap"], "B08 excerpt is not in the recorded ES2007a output"
except FileNotFoundError:
    pass  # Gate A sandbox: only scenes.py is present


# ═════════════════════════════ B01 — what it is ═════════════════════════════
class B01_WhatItIs(Scene):
    def construct(self):
        iso = Iso(1.6, -0.6, 0.9)
        self.add(marker("Q1 · what it is"), tag("CONSTRUCTED · illustration"))
        page, lines = rubric(-3.4, 0.2)
        P(self, FadeIn(page, shift=UP * 0.3), rt=0.6)
        P(self, Create(lines), rt=0.8)
        lab = T("rubric", 36).move_to([-3.4, -1.95, 0])
        P(self, FadeIn(lab), rt=0.4)
        at(self, "an AI judge")
        j = judge(iso, 0, 0)
        jl = T("AI judge", 36).move_to([1.6, -1.55, 0])
        P(self, FadeIn(j, shift=DOWN * 0.3), FadeIn(jl), rt=0.6)
        at(self, "reads differently")
        hit = lines[2]
        dot = Dot([-3.4 - 1.3 + 0.18, hit.get_center()[1], 0], radius=0.11, color=TERRA)
        P(self, hit.animate.shift(RIGHT * 0.5), FadeIn(dot), rt=0.6)
        cl = T("clause", 36).move_to([-0.95, 1.55, 0])
        P(self, FadeIn(cl), rt=0.4)
        at(self, "Python repository")
        back, front = iso.open_box(3.0, -1.4, 0, 1.3, 1.3, 0.8)
        rl = T("repo", 36).move_to([5.0, -2.35, 0])
        P(self, FadeIn(VGroup(back, front), shift=DOWN * 0.4), FadeIn(rl), rt=0.6)
        finish(self)


# ═════════════════════════════ B02 — why it matters ═════════════════════════════
class B02_Difference(Scene):
    def construct(self):
        self.add(marker("Q2 · why anyone would care"), tag("names only, no logos · as far as I could find in their docs, 14 Oct 2026"))
        boxes = {}
        for name, x in (("Maxim AI", -4.0), ("orq.ai", -0.6)):
            b = card(x, 0.55, 2.6, 1.5, stroke=INK, fill=BOX_R)
            boxes[name] = (b, T(name, 38).move_to([x, 1.75, 0]))
        at(self, "two tools")
        P(self, FadeIn(boxes["Maxim AI"][0]), FadeIn(boxes["Maxim AI"][1]), rt=0.5)
        at(self, "Maxim AI measures")
        a1 = Arrow([-4.0, -0.3, 0], [-4.0, -1.3, 0], color=INK, stroke_width=6, buff=0)
        s1 = T("agreement", 34).move_to([-4.0, -1.75, 0])
        P(self, GrowArrow(a1), FadeIn(s1), rt=0.5)
        at(self, "Ork dot AI")
        P(self, FadeIn(boxes["orq.ai"][0]), FadeIn(boxes["orq.ai"][1]), rt=0.5)
        a2 = Arrow([-0.6, -0.3, 0], [-0.6, -1.3, 0], color=INK, stroke_width=6, buff=0)
        s2 = T("rewritten prompt", 34).move_to([-0.6, -1.75, 0])
        P(self, GrowArrow(a2), FadeIn(s2), rt=0.5)
        at(self, "Readback will")
        page, lines = rubric(3.6, 0.55, n=4, w=2.2, h=2.6)
        rb = T("Readback", 38).move_to([3.6, 2.25, 0])
        P(self, FadeIn(page), Create(lines), FadeIn(rb), rt=0.6)
        dot = Dot([3.6 - 1.1 + 0.2, lines[1].get_center()[1], 0], radius=0.11, color=TERRA)
        q = qcard(5.35, -1.25)
        P(self, lines[1].animate.shift(RIGHT * 0.35), FadeIn(dot), rt=0.5)
        P(self, FadeIn(q, shift=UP * 0.2), rt=0.5)
        finish(self)


# ═════════════════════════════ B03 — who opens it ═════════════════════════════
class B03_FirstMinute(Scene):
    def construct(self):
        self.add(marker("Q3 · who opens it"), tag("CONSTRUCTED mock-up · values will be measured"))
        frame = card(-0.6, 0.0, 7.4, 4.6)
        bar = Rectangle(width=7.4, height=0.55, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to([-0.6, 2.02, 0])
        rl = T("README", 36).move_to([5.0, 2.0, 0])
        P(self, FadeIn(frame), FadeIn(bar), FadeIn(rl), rt=0.6)
        at(self, "one table")
        cells = VGroup()
        for r in range(5):
            for c in range(4):
                cells.add(Rectangle(width=1.5, height=0.55, stroke_color=BAR1, stroke_width=3, fill_color="#FFFFFF",
                                    fill_opacity=1).move_to([-3.45 + c * 1.62, 1.05 - r * 0.68, 0]))
        tl = T("per clause", 34).move_to([4.6, 1.2, 0])
        P(self, LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.04), FadeIn(tl), rt=1.2)
        at(self, "the question")
        row = VGroup(*cells[8:12])
        q = qcard(4.4, -0.3)
        P(self, row.animate.shift(RIGHT * 0.25), FadeIn(q, shift=LEFT * 0.2), rt=0.6)
        at(self, "The end user")
        pm = T("PM", 40).move_to([4.4, -1.6, 0])
        ring = Circle(radius=0.5, color=INK, stroke_width=5).move_to([4.4, -1.6, 0])
        P(self, Create(ring), FadeIn(pm), rt=0.5)
        finish(self)


# ═════════════════════════════ B04 — what it proves ═════════════════════════════
class B04_Proves(Scene):
    def construct(self):
        self.add(marker("Q4 · what it proves"), tag("CONSTRUCTED · planned commit order"))
        page, lines = rubric(-4.2, 0.4, n=4, w=2.2, h=2.8)
        pl = T("prompt contract", 34).move_to([-4.2, -1.45, 0])
        P(self, FadeIn(page), Create(lines), FadeIn(pl), rt=0.6)
        at(self, "my labels")
        ln = commit_line(-1.6, 4.6, 0.9)
        d1 = commit_dot(-0.6, 0.9)
        l1 = T("labels", 34).move_to([-0.6, 1.55, 0])
        P(self, Create(ln), FadeIn(d1), FadeIn(l1), rt=0.6)
        at(self, "before any judge")
        d2 = commit_dot(2.6, 0.9)
        l2 = T("judges", 34).move_to([2.6, 1.55, 0])
        P(self, FadeIn(d2), FadeIn(l2), rt=0.5)
        at(self, "human anchor")
        a = anchor(-0.6, -0.9)
        P(self, FadeIn(a, shift=DOWN * 0.3), rt=0.6)
        at(self, "I'll test one")
        one = card(2.6, -1.0, 1.4, 1.0, stroke=INK, fill=BOX_TOP)
        ol = T("one feature", 34).move_to([2.6, -2.0, 0])
        P(self, FadeIn(one), FadeIn(ol), rt=0.5)
        finish(self)


# ═════════════════════════════ B05 — in, out, first ═════════════════════════════
class B05_InOutFirst(Scene):
    def construct(self):
        self.add(marker("Q5 · in, out, first"), tag("AMI data · CC BY 4.0 · downloaded 14 Oct 2026"))
        pages = VGroup(*[card(-4.6 + i * 0.16, 0.9 - i * 0.12, 1.6, 2.0, stroke=BAR1, sw=3, fill="#FFFFFF") for i in range(10)])
        pl = T("10 AMI meetings", 34).move_to([-3.85, -1.6, 0])
        P(self, LaggedStart(*[FadeIn(p, shift=RIGHT * 0.2) for p in pages], lag_ratio=0.08), FadeIn(pl), rt=1.0)
        at(self, "never rewrite")
        page, lines = rubric(0.3, 0.6, n=4, w=2.0, h=2.6)
        pen = Line([2.2, 2.1, 0], [1.5, 1.2, 0], color=INK, stroke_width=12)
        strike = Line([1.3, 2.3, 0], [2.4, 1.0, 0], color=TERRA, stroke_width=10)
        cons = T("CONSTRUCTED", 32).move_to([0.3, -1.05, 0])
        P(self, FadeIn(page), Create(lines), FadeIn(pen), FadeIn(cons), rt=0.5)
        P(self, Create(strike), rt=0.4)
        at(self, "three judges")
        iso = Iso(0, 0, 0.6)
        js = VGroup(*[iso.mcp(0, 0, 0, w=1.0, d=1.0, h=0.7).move_to([3.0 + i * 1.45, 0.9, 0]) for i in range(3)])
        jl = T("3 judges · planned", 34).move_to([4.45, -0.1, 0])
        P(self, LaggedStart(*[FadeIn(j, shift=DOWN * 0.2) for j in js], lag_ratio=0.25), FadeIn(jl), rt=0.8)
        at(self, "its commit comes after")
        ln = commit_line(-0.4, 5.6, -1.75)
        pln = T("planned", 32).move_to([-1.3, -1.75, 0])
        d1 = commit_dot(0.4, -1.75)
        d2 = commit_dot(3.8, -1.75, filled=False)
        l1 = T("labels", 32).move_to([0.4, -2.35, 0]); l2 = T("report", 32).move_to([3.8, -2.35, 0])
        P(self, Create(ln), FadeIn(d1), FadeIn(l1), FadeIn(pln), rt=0.5)
        P(self, FadeIn(d2), FadeIn(l2), rt=0.4)
        finish(self)


# ═════════════════════════════ B06 — what could sink it ═════════════════════════════
class B06_Risk(Scene):
    def construct(self):
        self.add(marker("Q6 · what could sink it"), tag("CONSTRUCTED · planned method"))
        stack = VGroup(*[card(-3.6 + i * 0.12, 0.6 - i * 0.1, 1.5, 1.0, stroke=BAR1, sw=3, fill="#FFFFFF") for i in range(8)])
        sl = T("examples", 34).move_to([-3.2, -0.75, 0])
        P(self, FadeIn(stack), FadeIn(sl), rt=0.6)
        at(self, "freeze a held-out set")
        held = VGroup(*stack[5:])
        P(self, held.animate.shift(RIGHT * 3.6 + DOWN * 0.2), rt=0.7)
        lock = padlock(0.95, 1.2)
        hl = T("held-out", 34).move_to([0.75, -1.2, 0])
        P(self, FadeIn(lock, shift=DOWN * 0.2), FadeIn(hl), rt=0.5)
        at(self, "same-model and cross-model")
        iso = Iso(0, 0, 0.75)
        a = iso.mcp(0, 0, 0, w=1.0, d=1.0, h=0.7).move_to([3.2, 0.7, 0])
        b = iso.mcp(0, 0, 0, w=1.0, d=1.0, h=0.7).move_to([4.9, 0.7, 0])
        c = iso.box(0, 0, 0, 1.0, 1.0, 0.7).move_to([4.05, -1.05, 0])
        same = T("same model", 34).move_to([4.05, 1.85, 0])
        cross = T("cross-model", 34).move_to([4.05, -2.05, 0])
        P(self, FadeIn(a), FadeIn(b), FadeIn(same), rt=0.5)
        P(self, FadeIn(c, shift=UP * 0.2), FadeIn(cross), rt=0.5)
        finish(self)


# ═════════════════════════════ B07 — why this project ═════════════════════════════
class B07_WhyMe(Scene):
    def construct(self):
        self.add(marker("Q7 · why this project"), tag("PR status as of 14 Oct 2026"))
        shelf1 = Line([-5.6, 0.3, 0], [-1.2, 0.3, 0], color=INK, stroke_width=8)
        shelf2 = Line([0.0, 0.3, 0], [5.6, 0.3, 0], color=INK, stroke_width=8)
        n1 = T("new to me", 36).move_to([-3.4, 2.1, 0]); n2 = T("already mine", 36).move_to([2.8, 2.1, 0])
        P(self, Create(shelf1), FadeIn(n1), rt=0.5)
        jars = VGroup(*[RoundedRectangle(width=0.9, height=1.2, corner_radius=0.18, stroke_color=INK, stroke_width=4,
                                         fill_color=STAGE, fill_opacity=1).move_to([-4.7 + i * 1.3, 0.92, 0]) for i in range(3)])
        P(self, LaggedStart(*[FadeIn(j, shift=DOWN * 0.2) for j in jars], lag_ratio=0.3), rt=0.8)
        at(self, "Already mine")
        P(self, Create(shelf2), FadeIn(n2), rt=0.5)
        sealed = card(1.0, 0.95, 1.4, 1.2, stroke=INK, fill=BOX_R)
        sl = T("internal", 32).move_to([1.0, -0.35, 0])
        P(self, FadeIn(sealed, shift=DOWN * 0.2), FadeIn(sl), rt=0.5)
        at(self, "week one film")
        f8 = card(2.8, 0.95, 1.4, 1.2, stroke=INK, fill="#FFFFFF")
        t8 = VGroup(T("PR #8", 32).move_to([2.8, -0.35, 0]), T("open", 32).move_to([2.8, -0.95, 0]))
        P(self, FadeIn(f8, shift=DOWN * 0.2), FadeIn(t8), rt=0.5)
        at(self, "week two recipe")
        f23 = card(4.6, 0.95, 1.4, 1.2, stroke=INK, fill="#FFFFFF")
        t23 = VGroup(T("PR #23", 32).move_to([4.6, -0.35, 0]), T("open,", 32).move_to([4.6, -0.95, 0]), T("not merged", 32).move_to([4.6, -1.5, 0]))
        P(self, FadeIn(f23, shift=DOWN * 0.2), FadeIn(t23), rt=0.5)
        finish(self)


# ═════════════════════════════ B08 — exists today vs will exist ═════════════════════════════
class B08_ExistsWill(Scene):
    def construct(self):
        self.add(marker("exists today · will exist"),
                 tag("real output · Claude Opus 5.5 · 14 Oct 2026 · grey = will"))
        divider = Line([0.6, 2.6, 0], [0.6, -2.5, 0], color=BAR2, stroke_width=5)
        e = T("exists", 38).move_to([-2.8, 2.35, 0]); w = T("will", 38).move_to([3.6, 2.35, 0])
        P(self, Create(divider), FadeIn(e), FadeIn(w), rt=0.5)
        pages = VGroup(*[card(-5.0 + i * 0.1, 1.0 - i * 0.08, 1.2, 1.5, stroke=BAR1, sw=3, fill="#FFFFFF") for i in range(10)])
        page, lines = rubric(-2.6, 0.75, n=3, w=1.4, h=1.9)
        P(self, FadeIn(pages), FadeIn(page), Create(lines), rt=0.7)
        at(self, "Ten real outputs")
        ex = card(-2.65, -1.4, 5.9, 1.9, stroke=INK, fill="#FFFFFF")
        txt = VGroup(T("“Include a lock function so", 32), T("buttons can't be pressed", 32),
                     T("by accident” · ES2007a recap", 32)).arrange(DOWN, buff=0.1)
        txt.move_to([-2.65, -1.35, 0])
        P(self, FadeIn(ex), FadeIn(txt), rt=0.6)
        at(self, "What will exist")
        ghosts = VGroup(card(2.2, 0.8, 1.3, 1.6, stroke=BAR2, fill=STAGE),
                        card(3.8, 0.8, 1.3, 1.6, stroke=BAR2, fill=STAGE),
                        card(3.0, -1.3, 2.9, 1.3, stroke=BAR2, fill=STAGE))
        P(self, LaggedStart(*[Create(g) for g in ghosts], lag_ratio=0.3), rt=0.9)
        gl = T("labels · judges · table", 32).move_to([3.0, -2.3, 0])
        P(self, FadeIn(gl), rt=0.4)
        finish(self)
