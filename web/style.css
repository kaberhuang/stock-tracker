* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

[hidden] {
  display: none !important;
}

body {
  min-height: 100vh;
  font-family: "Segoe UI", "Microsoft JhengHei", sans-serif;
  background: linear-gradient(135deg, #0b1220 0%, #111827 45%, #1f2937 100%);
  color: #f8fafc;
}

.layout {
  display: grid;
  grid-template-columns: minmax(280px, 340px) 1fr;
  height: 100vh;
  overflow: hidden;
}

.sidebar {
  padding: 28px 22px;
  border-right: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(12px);
  overflow: auto;
}

.sidebar-header h1 {
  font-size: 1.5rem;
  margin-bottom: 6px;
}

.subtitle {
  color: #94a3b8;
  font-size: 0.92rem;
  line-height: 1.5;
  margin-bottom: 22px;
}

.add-form label {
  display: block;
  margin-bottom: 8px;
  color: #94a3b8;
  font-size: 0.9rem;
}

.add-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 8px;
  margin-bottom: 22px;
}

.add-row input {
  width: 100%;
  padding: 12px 14px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(15, 23, 42, 0.8);
  color: #f8fafc;
}

.add-row input:focus {
  outline: none;
  border-color: #22c55e;
}

button {
  border: none;
  border-radius: 12px;
  background: #22c55e;
  color: #052e16;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s ease;
}

.add-row button {
  padding: 0 16px;
}

button:hover {
  background: #16a34a;
}

.ghost-btn {
  padding: 6px 10px;
  background: rgba(255, 255, 255, 0.08);
  color: #cbd5e1;
  font-size: 0.82rem;
  font-weight: 600;
}

.ghost-btn:hover {
  background: rgba(255, 255, 255, 0.14);
}

.watchlist-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  color: #94a3b8;
  font-size: 0.9rem;
}

.watchlist {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: calc(100vh - 420px);
  overflow: auto;
}

.watch-item {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 10px;
  align-items: center;
  padding: 12px 14px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid transparent;
  cursor: pointer;
  transition: border-color 0.2s ease, background 0.2s ease;
}

.watch-item:hover,
.watch-item.active {
  border-color: rgba(34, 197, 94, 0.35);
  background: rgba(34, 197, 94, 0.08);
}

.watch-item-main {
  min-width: 0;
}

.watch-item-symbol {
  font-weight: 700;
  font-size: 0.95rem;
}

.watch-item-name {
  color: #94a3b8;
  font-size: 0.82rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.watch-item-quote {
  text-align: right;
  min-width: 72px;
}

.watch-item-price {
  font-size: 0.88rem;
  font-weight: 600;
}

.watch-item-change {
  font-size: 0.78rem;
  margin-top: 2px;
}

.watch-item-change.up,
.change.up,
.positive {
  color: #4ade80;
}

.watch-item-change.down,
.change.down,
.negative {
  color: #f87171;
}

.watch-item-change.flat,
.change.flat {
  color: #94a3b8;
}

.remove-btn {
  padding: 4px 8px;
  background: rgba(248, 113, 113, 0.12);
  color: #fca5a5;
  font-size: 0.75rem;
}

.remove-btn:hover {
  background: rgba(248, 113, 113, 0.22);
}

.content {
  padding: 28px;
  overflow: auto;
}

.content.charts-fit-screen {
  height: 100vh;
  overflow: hidden;
  padding: 14px 18px;
  display: flex;
  flex-direction: column;
}

.content.charts-fit-screen .content-toolbar {
  margin-bottom: 10px;
  flex-shrink: 0;
}

.content-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  margin-bottom: 22px;
  flex-wrap: wrap;
}

.view-tabs {
  display: inline-flex;
  gap: 8px;
  padding: 4px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.view-tabs button {
  padding: 8px 18px;
  background: transparent;
  color: #94a3b8;
  font-size: 0.9rem;
  font-weight: 600;
}

.view-tabs button.active,
.view-tabs button:hover {
  background: rgba(34, 197, 94, 0.18);
  color: #bbf7d0;
}

.toolbar-updated {
  color: #64748b;
  font-size: 0.85rem;
}

.overview-panel {
  max-width: 1200px;
  margin: 0 auto;
}

.overview-summary {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
  margin-bottom: 18px;
}

.summary-card {
  padding: 16px 18px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
}

.summary-card span {
  display: block;
  color: #94a3b8;
  font-size: 0.82rem;
  margin-bottom: 6px;
}

.summary-card strong {
  font-size: 1.5rem;
}

.summary-card.up strong {
  color: #4ade80;
}

.summary-card.down strong {
  color: #f87171;
}

.summary-card.flat strong {
  color: #94a3b8;
}

.overview-table-wrap {
  overflow-x: auto;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.overview-table {
  width: 100%;
  border-collapse: collapse;
  min-width: 760px;
}

.overview-table th,
.overview-table td {
  padding: 14px 16px;
  text-align: left;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.overview-table th {
  color: #94a3b8;
  font-size: 0.82rem;
  font-weight: 600;
  white-space: nowrap;
  cursor: pointer;
  user-select: none;
}

.overview-table th:hover {
  color: #cbd5e1;
}

.overview-table th.sorted {
  color: #bbf7d0;
}

.overview-table tbody tr {
  cursor: pointer;
  transition: background 0.15s ease;
}

.overview-table tbody tr:hover,
.overview-table tbody tr.active {
  background: rgba(34, 197, 94, 0.08);
}

.overview-table tbody tr:last-child td {
  border-bottom: none;
}

.overview-table .symbol-cell {
  font-weight: 700;
  color: #22c55e;
}

.overview-table .name-cell {
  color: #cbd5e1;
  max-width: 220px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.overview-table .num-cell {
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.overview-hint {
  margin-top: 14px;
  color: #64748b;
  font-size: 0.85rem;
}

.charts-panel {
  max-width: 1400px;
  margin: 0 auto;
}

.charts-panel.is-dense {
  max-width: none;
}

.charts-toolbar {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 14px;
}

.charts-toolbar .period-tabs {
  position: relative;
  z-index: 2;
  width: 100%;
}

.charts-toolbar-actions {
  display: flex;
  justify-content: flex-end;
}

.charts-panel.is-fit-screen .charts-toolbar {
  flex-shrink: 0;
}

.chart-count-control {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #94a3b8;
  font-size: 0.88rem;
  white-space: nowrap;
}

.chart-count-control select {
  padding: 8px 12px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(15, 23, 42, 0.8);
  color: #f8fafc;
  font-size: 0.88rem;
}

.chart-count-control select:focus {
  outline: none;
  border-color: #22c55e;
}

.charts-pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  margin-bottom: 14px;
}

.charts-pagination span {
  color: #94a3b8;
  font-size: 0.88rem;
  min-width: 120px;
  text-align: center;
}

.charts-grid {
  display: grid;
  gap: 16px;
}

.charts-panel.is-fit-screen {
  flex: 1;
  min-height: 0;
  max-width: none;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.charts-panel.is-fit-screen .charts-toolbar {
  margin-bottom: 8px;
  flex-shrink: 0;
}

.charts-panel.is-fit-screen .charts-pagination {
  margin-bottom: 8px;
  flex-shrink: 0;
}

.charts-panel.is-fit-screen .overview-hint {
  display: none;
}

.charts-grid.is-fit-screen {
  flex: 1;
  min-height: 0;
  gap: 8px;
  overflow: hidden;
}

.charts-grid.is-fit-screen .chart-card {
  display: flex;
  flex-direction: column;
  min-height: 0;
  padding: 8px 10px;
  border-radius: 12px;
}

.charts-grid.is-fit-screen .chart-card-header {
  margin-bottom: 4px;
  flex-shrink: 0;
  gap: 6px;
}

.charts-grid.is-fit-screen .chart-card-symbol {
  font-size: 0.72rem;
  margin-bottom: 2px;
}

.charts-grid.is-fit-screen .chart-card-name {
  font-size: 0.76rem;
  line-height: 1.2;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.charts-grid.is-fit-screen .chart-card-price {
  font-size: 0.8rem;
}

.charts-grid.is-fit-screen .chart-card-change,
.charts-grid.is-fit-screen .chart-card-trend {
  font-size: 0.68rem;
}

.charts-grid.is-fit-screen .mini-chart-wrap {
  flex: 1;
  min-height: 0;
  height: auto;
}

.charts-grid.is-dense {
  gap: 12px;
}

.charts-grid.is-dense .mini-chart-wrap {
  height: 120px;
}

.charts-grid.is-dense .chart-card {
  padding: 12px;
}

.charts-grid.is-dense .chart-card-name {
  font-size: 0.9rem;
}

.chart-card {
  padding: 16px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  cursor: grab;
  touch-action: none;
  user-select: none;
  transition: border-color 0.2s ease, background 0.2s ease, transform 0.15s ease;
}

.chart-card:hover,
.chart-card.active {
  border-color: rgba(34, 197, 94, 0.35);
  background: rgba(34, 197, 94, 0.06);
}

.chart-card-header {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: flex-start;
  margin-bottom: 12px;
}

.chart-card-title {
  min-width: 0;
}

.chart-card.is-dragging {
  opacity: 0.55;
  pointer-events: none;
  cursor: grabbing;
  z-index: 2;
  position: relative;
}

.chart-card.is-drag-over {
  border-color: rgba(34, 197, 94, 0.65);
  background: rgba(34, 197, 94, 0.1);
  transform: scale(1.01);
}

.chart-card.is-dragging,
.chart-card.is-drag-over {
  cursor: grabbing;
}

.mini-chart-wrap,
.mini-chart-wrap canvas,
.mini-chart-wrap > div {
  pointer-events: none;
}

.chart-card-symbol {
  color: #22c55e;
  font-weight: 700;
  font-size: 0.88rem;
  margin-bottom: 4px;
}

.chart-card-name {
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.4;
}

.chart-card-quote {
  text-align: right;
  flex-shrink: 0;
}

.chart-card-price {
  display: block;
  font-size: 1.15rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.chart-card-change {
  display: block;
  margin-top: 4px;
  font-size: 0.85rem;
  font-weight: 600;
}

.chart-card-trend {
  margin-top: 6px;
  color: #64748b;
  font-size: 0.78rem;
}

.mini-chart-wrap {
  position: relative;
  height: 160px;
}

.empty-state {
  max-width: 560px;
  margin: 80px auto 0;
  text-align: center;
}

.empty-state h2 {
  font-size: 1.6rem;
  margin-bottom: 10px;
}

.empty-state p,
.examples {
  color: #94a3b8;
  line-height: 1.7;
}

.examples {
  list-style: none;
  margin-top: 24px;
  text-align: left;
  display: inline-block;
}

.examples li {
  margin-bottom: 8px;
}

.detail-panel {
  max-width: 1100px;
  margin: 0 auto;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  align-items: flex-start;
  margin-bottom: 24px;
}

.symbol-label {
  color: #22c55e;
  font-weight: 700;
  margin-bottom: 4px;
}

.detail-header h2 {
  font-size: 1.8rem;
}

.price-block {
  text-align: right;
}

.price-row {
  display: flex;
  justify-content: flex-end;
  align-items: baseline;
  gap: 8px;
}

.price {
  font-size: 2.4rem;
  font-weight: 700;
}

.currency {
  color: #94a3b8;
}

.change {
  margin-top: 4px;
  font-size: 1rem;
  font-weight: 600;
}

.updated-at {
  margin-top: 6px;
  color: #64748b;
  font-size: 0.85rem;
}

.period-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 18px;
}

.period-tabs button {
  padding: 8px 14px;
  background: rgba(255, 255, 255, 0.06);
  color: #cbd5e1;
  font-size: 0.88rem;
  font-weight: 600;
}

.period-tabs button.active,
.period-tabs button:hover {
  background: rgba(34, 197, 94, 0.18);
  color: #bbf7d0;
}

.chart-wrap {
  padding: 18px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  margin-bottom: 18px;
  min-height: 280px;
}

.chart-wrap canvas {
  display: block;
  width: 100% !important;
}

.trend-summary,
.stats-grid {
  display: grid;
  gap: 12px;
  margin-bottom: 18px;
}

.trend-summary {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.stats-grid {
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
}

.stat-card {
  padding: 14px 16px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
}

.stat-card span {
  display: block;
  color: #94a3b8;
  font-size: 0.82rem;
  margin-bottom: 6px;
}

.stat-card strong {
  font-size: 1rem;
}

.note {
  margin-top: 24px;
  color: #64748b;
  font-size: 0.84rem;
  line-height: 1.6;
}

code {
  color: #cbd5e1;
}

.loading {
  opacity: 0.6;
}

.overview-panel.loading {
  pointer-events: none;
}

.charts-panel.loading .charts-toolbar,
.charts-panel.loading .charts-pagination {
  opacity: 1;
  pointer-events: auto;
}

.charts-panel.loading .charts-grid,
.charts-panel.loading .charts-pagination,
.detail-panel.loading .chart-wrap,
.detail-panel.loading .trend-summary,
.detail-panel.loading .stats-grid {
  opacity: 0.6;
  pointer-events: none;
}

.detail-panel.loading .detail-header,
.detail-panel.loading .period-tabs {
  opacity: 1;
  pointer-events: auto;
}

@media (max-width: 960px) {
  .layout {
    grid-template-columns: 1fr;
    height: auto;
    overflow: visible;
  }

  .content.charts-fit-screen {
    height: auto;
    overflow: visible;
  }

  .charts-panel.is-fit-screen {
    overflow: visible;
  }

  .charts-grid.is-fit-screen {
    overflow: visible;
    grid-template-rows: none !important;
  }

  .charts-grid.is-fit-screen .mini-chart-wrap {
    height: 120px;
    flex: none;
  }

  .sidebar {
    border-right: none;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }

  .watchlist {
    max-height: 240px;
  }

  .detail-header {
    flex-direction: column;
  }

  .price-block {
    text-align: left;
  }

  .price-row {
    justify-content: flex-start;
  }

  .trend-summary {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .overview-summary {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .content-toolbar {
    flex-direction: column;
    align-items: flex-start;
  }

  .charts-grid {
    grid-template-columns: 1fr !important;
  }

  .charts-toolbar-actions {
    justify-content: stretch;
  }

  .chart-count-control {
    width: 100%;
    justify-content: space-between;
  }
}
