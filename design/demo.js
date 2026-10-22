/* ---------- DEMO page: everything works, but orders and slips are only simulated (nothing reaches the real list) ---------- */
(function () {
  var n = 0;
  postOrder = function (payload) {
    var v = priced(payload), c = calc(v);
    var o = { id: 'DEMO' + (++n), cid: payload.cid, ts: new Date().toISOString(), name: payload.name, hoodFree: v.hoodFree, hood: v.hood,
      hoodUnits: v.hoodUnits.map(function (u) { return { size: u.size, name: u.name, free: u.free }; }), tee: v.tee, umbrella: v.umbrella, note: payload.note, total: c.total };
    var mine = H.email === normEmail(payload.email) ? H.orders : [];
    return wait(600).then(function () { return { ok: true, order: o, orders: mine.concat([o]), slips: H.slips, mailed: false }; });
  };
  postSlip = function (payload) {
    var s = { id: 'SDEMO' + (++n), cid: payload.cid, ts: new Date().toISOString(), amount: payload.amount, checked: false, ocr: 'match', rejected: false, reason: '' };
    return wait(900).then(function () { return { ok: true, slip: s, slips: H.slips.concat([s]), mailed: false }; });
  };
})();
