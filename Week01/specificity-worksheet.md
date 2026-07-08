# Specificity Worksheet

## Objective
Manually calculate CSS specificity for 6-8 overlapping selectors targeting the
same element, predict the winning rule, then verify using Chrome DevTools.

## Test Element
```html
<div id="main">
  <p class="text highlight">Which color am I?</p>
</div>
```

## Specificity Calculations

| # | Selector | IDs | Classes/Attr/Pseudo | Elements | Specificity (ID, Class, Element) |
|---|---|---|---|---|---|
| 1 | `p` | 0 | 0 | 1 | (0,0,1) |
| 2 | `.text` | 0 | 1 | 0 | (0,1,0) |
| 3 | `#main p` | 1 | 0 | 1 | (1,0,1) |
| 4 | `div p.text` | 0 | 1 | 2 | (0,1,2) |
| 5 | `#main .text` | 1 | 1 | 0 | (1,1,0) |
| 6 | `p.text.highlight` | 0 | 2 | 1 | (0,2,1) |
| 7 | `div#main p.text.highlight` | 1 | 2 | 2 | (1,2,2) |
| 8 | `.text.highlight` | 0 | 2 | 0 | (0,2,0) |

## Prediction
Comparing specificity left to right (IDs → Classes → Elements), the rule with
the highest ID count wins first. Rules 3, 5, and 7 all have 1 ID.
Among those, Rule 7 (`div#main p.text.highlight`) has the most classes (2)
and elements (2), so it should win.

**Predicted winner:** Rule 7 — `div#main p.text.highlight` → color: teal

## DevTools Verification
Opened `specificity-demo/index.html` in Chrome → Inspected the `<p>` element →
checked the Styles panel.

**Actual winner:** [write the color/rule you actually saw at the top, un-struck-through]

**Result:** ✅ Prediction confirmed / ❌ Prediction was wrong

(Screenshot attached: `specificity-devtools.png`)

## Key Takeaway
Specificity is compared as three separate counts (IDs, classes, elements) —
not added together as one number. A selector with 1 ID always beats any
selector with only classes and elements, no matter how many of those it has.
Source order only matters as a tiebreaker when specificity scores are exactly equal.