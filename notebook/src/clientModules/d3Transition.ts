// Workaround for d3@7.9.2 declaring `"sideEffects": false` in its package.json.
// Mermaid imports `select` from `d3` and calls `.transition()` on selections,
// expecting `d3-transition` to have patched `Selection.prototype.transition`.
// Bundlers tree-shake `d3-transition` out of the `d3` barrel unless it is
// imported directly.
import 'd3-transition';
