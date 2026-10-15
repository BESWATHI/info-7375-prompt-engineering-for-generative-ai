# ═════════════════════════════ Source Check pitch — scenes ═════════════════════════════
# Assembled into ../scenes.py by code/build_scenes.py (iso_kit + iso_originals_25 + this file),
# because Gate A copies only scenes.py. Timing rule used by every scene (show-tell gate traps):
#   phase 1 (0 → ≤ 0.38·D): the prop, its label(s) and the "proposed design" tag are on screen;
#   nothing moves in the 0.42–0.58·D window that GATE T / Gate V sample;
#   phase 2 (≥ 0.62·D): the second action, which always ADDS a new non-text shape (Gate A).

PHASE2 = 0.62


def _D(self):
    return _TARGET.get(type(self).__name__.split("_")[0], 8.0) or 8.0


def go(self, t):
    """Wait until absolute scene time t (seconds)."""
    gap = t - _elapsed(self)
    if gap > 0.04:
        self.wait(gap)


def below(mob, text, size=36, gap=0.45):
    lab = T(text, size)
    lab.move_to(np.array(mob.get_bottom()) + np.array([0, -gap - lab.height / 2, 0]))
    return lab


def beside(mob, text, size=36, gap=0.45, side=RIGHT):
    lab = T(text, size)
    edge = np.array(mob.get_right()) if side is RIGHT else np.array(mob.get_left())
    sign = 1 if side is RIGHT else -1
    lab.move_to(edge + np.array([sign * (gap + lab.width / 2), 0, 0]))
    return lab


def tag():
    """Honesty tag on every drawn pitch beat: this is a design, not a built system."""
    t = T("proposed design", 32)
    t.move_to(np.array([6.1 - t.width / 2, 3.15 - t.height / 2, 0]))
    return t


def person(x, y, s=1.0):
    head = Circle(radius=0.26 * s, fill_color=DARK_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y + 0.62 * s, 0])
    body = Polygon([x - 0.42 * s, y - 0.45 * s, 0], [x + 0.42 * s, y - 0.45 * s, 0], [x + 0.3 * s, y + 0.25 * s, 0],
                   [x - 0.3 * s, y + 0.25 * s, 0], fill_color=DARK_L, fill_opacity=1, stroke_color=INK, stroke_width=4)
    return VGroup(body, head)


def flat_page(x, y, w=1.35, h=1.7, ghost=False):
    """A plain page seen straight on (claims, logs, tests)."""
    if ghost:
        return DashedVMobject(Rectangle(width=w, height=h, stroke_color=BAR1, stroke_width=4), num_dashes=24).move_to([x, y, 0])
    card = Rectangle(width=w, height=h, fill_color="#FFFFFF", fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    lines = VGroup(*[Line([x - w / 2 + 0.18, y + h * f, 0], [x + w / 2 - 0.18, y + h * f, 0], color=BAR2, stroke_width=5)
                     for f in (0.22, 0.04, -0.14)])
    dot = Dot([x - w / 2 + 0.22, y + h * 0.36, 0], radius=0.06, color=TERRA)
    return VGroup(card, lines, dot)


class B00_RealCase(Scene):
    def construct(self):
        D = _D(self)
        belt = make_original("conveyor", height=3.4, x=-2.7, y=-0.4)
        lab = below(belt, "chatbot answer")
        self.play(FadeIn(belt), FadeIn(lab), run_time=0.8)
        self.play(belt.parts["parcel"].animate.shift(belt.action_vectors["parcel"] * 1.0), run_time=1.0)
        go(self, PHASE2 * D)
        pol = make_original("skill-stack", height=2.6, x=3.4, y=0.2)
        plab = below(pol, "policy: before")
        cap = T("Moffatt v. Air Canada, 2024", 34)
        cap.move_to([0, 2.95, 0])
        self.play(FadeIn(pol), FadeIn(plab), FadeIn(cap), run_time=0.8)
        finish(self)


class B01_Scanner(Scene):
    def construct(self):
        D = _D(self)
        sc = make_original("checkpoint-scanner", height=4.0, x=-1.0, y=-0.1)
        lab = beside(sc, "Source Check", 40)
        self.play(FadeIn(sc), FadeIn(lab), FadeIn(tag()), run_time=0.8)
        go(self, PHASE2 * D)
        self.play(sc.parts["parcel"].animate.shift(sc.action_vectors["parcel"]), run_time=0.9)
        c = check(float(np.array(sc.get_right())[0]) + 0.4, -1.6, s=0.28)
        self.play(Create(c), run_time=0.5)
        finish(self)


class B02_Claims(Scene):
    def construct(self):
        D = _D(self)
        box = make_original("release-parcel", height=3.3, x=-3.3, y=0.1)
        lab = below(box, "bot's answer")
        self.play(FadeIn(box), FadeIn(lab), FadeIn(tag()), run_time=0.8)
        self.play(box.parts["lid"].animate.shift(box.action_vectors["lid"]), run_time=0.8)
        go(self, PHASE2 * D)
        pages = VGroup(*[flat_page(x, 0.3) for x in (0.9, 2.5, 4.1)])
        plab = T("claims", 36).move_to([2.5, -1.15, 0])
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.3) for p in pages], lag_ratio=0.25), FadeIn(plab), run_time=1.0)
        finish(self)


class B03_Versions(Scene):
    def construct(self):
        D = _D(self)
        sh = make_original("version-shelves", height=3.7, x=-3.4, y=0.2)
        lab = below(sh, "policy versions")
        self.play(FadeIn(sh), FadeIn(lab), FadeIn(tag()), run_time=0.8)
        self.play(sh.parts["selected-version"].animate.shift(sh.action_vectors["selected-version"]), run_time=0.9)
        go(self, PHASE2 * D)
        tr = make_original("comparison-trays", height=2.9, x=3.3, y=0.3)
        tlab = below(tr, "compare")
        self.play(FadeIn(tr), FadeIn(tlab), run_time=0.8)
        finish(self)


class B04_Pass(Scene):
    def construct(self):
        D = _D(self)
        g = make_original("permission-gate", height=3.7, x=-1.8, y=0.2)
        lab = below(g, "every claim matches")
        self.play(FadeIn(g), FadeIn(lab), FadeIn(tag()), run_time=0.7)
        self.play(g.parts["barrier"].animate.shift(g.action_vectors["barrier"]), run_time=0.8)
        go(self, PHASE2 * D)
        log = flat_page(3.6, 0.4)
        llab = below(log, "log: version used")
        c = check(4.45, 1.25, s=0.24)
        self.play(FadeIn(log), FadeIn(llab), Create(c), run_time=0.8)
        finish(self)


class B05_Hold(Scene):
    def construct(self):
        D = _D(self)
        h = make_original("human-handoff", height=3.3, x=-2.0, y=0.2)
        lab = below(h, "HOLD", 40)
        self.play(FadeIn(h), FadeIn(lab), FadeIn(tag()), run_time=0.7)
        self.play(h.parts["packet"].animate.shift(h.action_vectors["packet"]), run_time=0.9)
        go(self, PHASE2 * D)
        p = person(3.4, 0.2, s=1.3)
        plab = below(p, "a person decides")
        self.play(FadeIn(p), FadeIn(plab), run_time=0.8)
        finish(self)


class B06_Router(Scene):
    def construct(self):
        D = _D(self)
        # v1 used the branch-junction prop; its diagonal arm plates overlap and fail GATE T §8.6b,
        # so the route is drawn as a row: answer box in the middle, a "pass" tray and a "hold" tray.
        iso = Iso(0, -0.2, 0.9)
        box = iso.box(-0.6, -0.6, 0, 1.2, 1.2, 1.0)
        blab = T("n8n workflow", 36).move_to([0, -1.75, 0])
        trays = VGroup(make_original("context-inbox", height=1.5, x=-4.2, y=0.0),
                       make_original("context-inbox", height=1.5, x=4.2, y=0.0))
        tlabs = VGroup(below(trays[0], "pass", 36), below(trays[1], "hold", 36))
        self.play(FadeIn(box), FadeIn(blab), FadeIn(trays), FadeIn(tlabs), FadeIn(tag()), run_time=0.9)
        go(self, PHASE2 * D)
        self.play(box.animate.shift(RIGHT * 2.3 + UP * 0.25), run_time=0.9)
        dot = Dot([4.2, 1.05, 0], radius=0.1, color=TERRA)
        self.play(FadeIn(dot), run_time=0.4)
        finish(self)


class B07_Alternatives(Scene):
    def construct(self):
        # no 'proposed design' tag: this beat shows real things (v2)
        D = _D(self)
        trays = VGroup(*[make_original("context-inbox", height=1.45, x=x, y=0.3) for x in (-5.1, -2.65, -0.2)])
        labs = VGroup(*[below(t, s, 34) for t, s in zip(trays, ("Fin", "Zendesk", "manual"))])
        self.play(LaggedStart(*[FadeIn(t) for t in trays], lag_ratio=0.2), FadeIn(labs), run_time=1.1)
        go(self, PHASE2 * D)
        sc = make_original("checkpoint-scanner", height=2.9, x=4.1, y=0.45)
        slab = below(sc, "check before sending", 34)
        self.play(FadeIn(sc), FadeIn(slab), run_time=0.8)
        finish(self)


class B08_Demo(Scene):
    def construct(self):
        D = _D(self)
        w = make_original("agent-workstation", height=3.6, x=-2.5, y=0.2)
        lab = below(w, "one command")
        self.play(FadeIn(w), FadeIn(lab), FadeIn(tag()), run_time=0.7)
        self.play(w.parts["tool"].animate.shift(w.action_vectors["tool"]), run_time=0.8)
        go(self, PHASE2 * D)
        st = make_original("approval-stamp", height=2.7, x=3.4, y=0.3)
        slab = below(st, "HOLD + reason")
        self.play(FadeIn(st), FadeIn(slab), run_time=0.8)
        finish(self)


class B09_Evidence(Scene):
    def construct(self):
        D = _D(self)
        b = make_original("evidence-binder", height=2.9, x=-2.7, y=0.2)
        lab = below(b, "evidence")
        self.play(FadeIn(b), FadeIn(lab), FadeIn(tag()), run_time=0.7)
        self.play(b.parts["cover"].animate.shift(b.action_vectors["cover"]), run_time=0.8)
        go(self, PHASE2 * D)
        pages = VGroup(*[flat_page(x, 0.35, w=1.05, h=1.35) for x in (1.8, 3.4)])
        plabs = VGroup(below(pages[0], "tests", 34), below(pages[1], "eval log", 34))
        self.play(FadeIn(pages), FadeIn(plabs), run_time=0.8)
        finish(self)


class B10_FirstTest(Scene):
    def construct(self):
        D = _D(self)
        bench = make_original("experiment-bench", height=3.5, x=-1.8, y=0.2)
        lab = below(bench, "first test")
        self.play(FadeIn(bench), FadeIn(lab), FadeIn(tag()), run_time=0.7)
        self.play(bench.parts["sample"].animate.shift(bench.action_vectors["sample"]), run_time=0.9)
        go(self, PHASE2 * D)
        r = np.array(bench.get_right())
        dot = Dot([r[0] + 1.9, 0.45, 0], radius=0.12, color=TERRA)
        dlab = T("must be held", 36).move_to([r[0] + 1.9, -0.3, 0])
        self.play(FadeIn(dot), FadeIn(dlab), run_time=0.7)
        finish(self)


class B11_Risk(Scene):
    def construct(self):
        D = _D(self)
        lamp = make_original("inspection-lamp", height=3.8, x=-1.9, y=0.2)
        lab = below(lamp, "condition words")
        self.play(FadeIn(lamp), FadeIn(lab), FadeIn(tag()), run_time=0.7)
        self.play(lamp.parts["lamp-head"].animate.shift(lamp.action_vectors["lamp-head"]), run_time=0.9)
        go(self, PHASE2 * D)
        bef = T("before", 40).move_to([3.4, 0.8, 0])
        aft = T("after", 40).move_to([3.4, -0.3, 0])
        # an X beside "after" (a line through the label fails Gate B's label-on-line check)
        strike = VGroup(Line([2.25, -0.08, 0], [2.6, -0.48, 0], color=INK, stroke_width=7),
                        Line([2.6, -0.08, 0], [2.25, -0.48, 0], color=INK, stroke_width=7))
        dot = Dot([2.4, 0.8, 0], radius=0.1, color=TERRA)
        self.play(FadeIn(bef), FadeIn(aft), FadeIn(dot), run_time=0.6)
        self.play(Create(strike), run_time=0.4)
        finish(self)


class B12_Skills(Scene):
    def construct(self):
        # no 'proposed design' tag: this beat shows real things (v2)
        D = _D(self)
        st = make_original("skill-stack", height=3.1, x=-2.8, y=0.2)
        lab = below(st, "have: n8n, Claude")
        self.play(FadeIn(st), FadeIn(lab), run_time=0.7)
        go(self, PHASE2 * D)
        pg = flat_page(3.0, 0.4)
        plab = below(pg, "new: evaluation")
        self.play(FadeIn(pg, shift=UP * 0.3), FadeIn(plab), run_time=0.8)
        finish(self)


class B13_ExistsWill(Scene):
    def construct(self):
        # no 'proposed design' tag: this beat shows real things (v2)
        D = _D(self)
        left = VGroup(*[flat_page(x, 0.45, w=1.0, h=1.3) for x in (-5.0, -3.7, -2.4)])
        llab = T("exists today", 36).move_to([-3.7, -0.75, 0])
        self.play(LaggedStart(*[FadeIn(p) for p in left], lag_ratio=0.2), FadeIn(llab), run_time=1.0)
        go(self, PHASE2 * D)
        right = VGroup(*[flat_page(x, 0.45, w=1.0, h=1.3, ghost=True) for x in (2.2, 3.5, 4.8)])
        rlab = T("will exist", 36).move_to([3.5, -0.75, 0])
        self.play(LaggedStart(*[Create(p) for p in right], lag_ratio=0.2), FadeIn(rlab), run_time=1.0)
        finish(self)
