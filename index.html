const STORAGE_KEY = "stock-tracker-watchlist";
const CHART_COUNT_KEY = "stock-tracker-chart-count";
const VALID_CHART_COUNTS = [1, 2, 3, 4, 6, 8, 10, 12, 16, 20];
const DEFAULT_SYMBOLS = ["2330.TW", "0050.TW", "AAPL"];

const addForm = document.getElementById("add-form");
const symbolInput = document.getElementById("symbol-input");
const watchlistEl = document.getElementById("watchlist");
const refreshAllBtn = document.getElementById("refresh-all-btn");
const emptyState = document.getElementById("empty-state");
const overviewPanel = document.getElementById("overview-panel");
const chartsPanel = document.getElementById("charts-panel");
const chartsGrid = document.getElementById("charts-grid");
const detailPanel = document.getElementById("detail-panel");
const viewTabs = document.getElementById("view-tabs");
const periodTabs = document.getElementById("period-tabs");
const chartsPeriodTabs = document.getElementById("charts-period-tabs");
const chartDisplayCountSelect = document.getElementById("chart-display-count");
const chartsPagination = document.getElementById("charts-pagination");
const chartsPrevBtn = document.getElementById("charts-prev-btn");
const chartsNextBtn = document.getElementById("charts-next-btn");
const chartsPageLabel = document.getElementById("charts-page-label");
const overviewBody = document.getElementById("overview-body");
const overviewUpdated = document.getElementById("overview-updated");
const contentEl = document.querySelector(".content");

const summaryCount = document.getElementById("summary-count");
const summaryUp = document.getElementById("summary-up");
const summaryDown = document.getElementById("summary-down");
const summaryFlat = document.getElementById("summary-flat");

const detailSymbol = document.getElementById("detail-symbol");
const detailName = document.getElementById("detail-name");
const detailPrice = document.getElementById("detail-price");
const detailCurrency = document.getElementById("detail-currency");
const detailChange = document.getElementById("detail-change");
const detailUpdated = document.getElementById("detail-updated");

const trendChange = document.getElementById("trend-change");
const trendPercent = document.getElementById("trend-percent");
const trendStart = document.getElementById("trend-start");
const trendEnd = document.getElementById("trend-end");

const statPrevClose = document.getElementById("stat-prev-close");
const statDayHigh = document.getElementById("stat-day-high");
const statDayLow = document.getElementById("stat-day-low");
const statVolume = document.getElementById("stat-volume");
const stat52High = document.getElementById("stat-52-high");
const stat52Low = document.getElementById("stat-52-low");
const statMarketCap = document.getElementById("stat-market-cap");
const statPrevLabel = document.getElementById("stat-prev-label");
const statHighLabel = document.getElementById("stat-high-label");
const statLowLabel = document.getElementById("stat-low-label");
const stat52HighLabel = document.getElementById("stat-52-high-label");
const stat52LowLabel = document.getElementById("stat-52-low-label");
const statVolumeCard = document.getElementById("stat-volume-card");
const statMarketCapCard = document.getElementById("stat-market-cap-card");

const COLUMN_LABELS = {
  symbol: "代號",
  name: "名稱",
  price: "報價",
  change: "漲跌",
  change_percent: "漲跌幅",
  day_high: "最高",
  day_low: "最低",
  volume: "成交量",
};

const STAT_LABELS = {
  yield: {
    prev: "前日殖利率",
    high: "今日最高殖利率",
    low: "今日最低殖利率",
    week52High: "52 週最高殖利率",
    week52Low: "52 週最低殖利率",
  },
  bond_etf: {
    prev: "前日淨值",
    high: "今日最高",
    low: "今日最低",
    week52High: "52 週最高",
    week52Low: "52 週最低",
  },
  stock: {
    prev: "前一日收盤",
    high: "今日最高",
    low: "今日最低",
    week52High: "52 週最高",
    week52Low: "52 週最低",
  },
};

let watchlist = loadWatchlist();
let selectedSymbol = watchlist[0] || null;
let currentView = "overview";
let currentPeriod = "1mo";
let sortKey = "symbol";
let sortAsc = true;
let priceChart = null;
let miniCharts = {};
let quoteCache = {};
let historyCache = {};
let lastChartHistories = [];
let chartDisplayCount = loadChartDisplayCount();
let chartPageIndex = 0;
let chartDragState = null;

const CHART_DRAG_THRESHOLD = 8;

function loadChartDisplayCount() {
  const saved = localStorage.getItem(CHART_COUNT_KEY);
  if (saved === "all") {
    return "all";
  }
  const count = Number(saved);
  if (VALID_CHART_COUNTS.includes(count)) {
    return count;
  }
  return 4;
}

function getChartLayoutCount(visibleCount) {
  if (chartDisplayCount === "all") {
    return watchlist.length;
  }
  return Math.min(Number(chartDisplayCount), visibleCount);
}

function shouldUseFitScreenLayout(visibleCount) {
  const count = getChartLayoutCount(visibleCount);
  return count >= 8 && count <= 20;
}

function getGridLayout(visibleCount) {
  const count = getChartLayoutCount(visibleCount);

  if (count <= 1) {
    return { cols: 1, rows: 1 };
  }
  if (count <= 4) {
    return { cols: count, rows: 1 };
  }
  if (count <= 6) {
    return { cols: 3, rows: 2 };
  }
  if (count <= 8) {
    return { cols: 4, rows: 2 };
  }
  if (count <= 10) {
    return { cols: 5, rows: 2 };
  }
  if (count <= 12) {
    return { cols: 4, rows: 3 };
  }
  if (count <= 16) {
    return { cols: 4, rows: 4 };
  }
  if (count <= 20) {
    return { cols: 5, rows: 4 };
  }
  return { cols: 5, rows: Math.ceil(count / 5) };
}

function applyChartsGridLayout(visibleCount) {
  const layout = getGridLayout(visibleCount);
  const fitScreen = shouldUseFitScreenLayout(visibleCount);

  chartsGrid.className = "charts-grid";
  chartsPanel.classList.remove("is-dense", "is-fit-screen");
  chartsGrid.classList.remove("is-dense", "is-fit-screen");
  chartsGrid.style.gridTemplateColumns = "";
  chartsGrid.style.gridTemplateRows = "";

  if (chartDisplayCount === "all" && watchlist.length > 20) {
    chartsGrid.style.gridTemplateColumns = "repeat(auto-fill, minmax(260px, 1fr))";
    chartsPanel.classList.add("is-dense");
    chartsGrid.classList.add("is-dense");
    updateContentFitMode(false);
    return;
  }

  if (fitScreen) {
    chartsPanel.classList.add("is-fit-screen");
    chartsGrid.classList.add("is-fit-screen");
    chartsGrid.style.gridTemplateColumns = `repeat(${layout.cols}, minmax(0, 1fr))`;
    chartsGrid.style.gridTemplateRows = `repeat(${layout.rows}, minmax(0, 1fr))`;
    updateContentFitMode(true);
    return;
  }

  chartsGrid.style.gridTemplateColumns = `repeat(${layout.cols}, minmax(0, 1fr))`;

  if (Number(chartDisplayCount) > 6 || (chartDisplayCount === "all" && watchlist.length > 6)) {
    chartsPanel.classList.add("is-dense");
    chartsGrid.classList.add("is-dense");
  }

  updateContentFitMode(false);
}

function updateContentFitMode(enabled) {
  contentEl.classList.toggle("charts-fit-screen", enabled && currentView === "charts");
}

function saveChartDisplayCount() {
  localStorage.setItem(CHART_COUNT_KEY, String(chartDisplayCount));
}

function getChartPageSize() {
  return chartDisplayCount === "all" ? watchlist.length : chartDisplayCount;
}

function getTotalChartPages() {
  const pageSize = getChartPageSize();
  if (pageSize <= 0) {
    return 1;
  }
  return Math.max(1, Math.ceil(watchlist.length / pageSize));
}

function clampChartPageIndex() {
  const totalPages = getTotalChartPages();
  if (chartPageIndex >= totalPages) {
    chartPageIndex = totalPages - 1;
  }
  if (chartPageIndex < 0) {
    chartPageIndex = 0;
  }
}

function getVisibleChartSymbols() {
  if (chartDisplayCount === "all") {
    return watchlist;
  }
  clampChartPageIndex();
  const start = chartPageIndex * chartDisplayCount;
  return watchlist.slice(start, start + chartDisplayCount);
}

function updateChartsPagination() {
  const pageSize = getChartPageSize();
  const needsPagination = chartDisplayCount !== "all" && watchlist.length > pageSize;

  chartsPagination.hidden = !needsPagination;
  if (!needsPagination) {
    return;
  }

  clampChartPageIndex();
  chartsPageLabel.textContent = `第 ${chartPageIndex + 1} / ${getTotalChartPages()} 頁`;
  chartsPrevBtn.disabled = chartPageIndex <= 0;
  chartsNextBtn.disabled = chartPageIndex >= getTotalChartPages() - 1;
}

function syncChartDisplayControls() {
  chartDisplayCountSelect.value = String(chartDisplayCount);
}

function loadWatchlist() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    if (Array.isArray(saved) && saved.length > 0) {
      return [...new Set(saved.map((item) => String(item).trim().toUpperCase()))];
    }
  } catch {
    // ignore invalid storage
  }
  return [...DEFAULT_SYMBOLS];
}

function saveWatchlist() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(watchlist));
}

function reorderWatchlist(fromSymbol, toSymbol) {
  const fromIndex = watchlist.indexOf(fromSymbol);
  const toIndex = watchlist.indexOf(toSymbol);
  if (fromIndex === -1 || toIndex === -1 || fromIndex === toIndex) {
    return false;
  }

  watchlist.splice(fromIndex, 1);
  watchlist.splice(toIndex, 0, fromSymbol);
  saveWatchlist();
  return true;
}

function ensureSelectedSymbol() {
  if (!selectedSymbol && watchlist.length > 0) {
    selectedSymbol = watchlist[0];
  }
}

function findChartDropTarget(clientX, clientY, draggedCard) {
  return [...chartsGrid.querySelectorAll(".chart-card")].find((card) => {
    if (card === draggedCard) {
      return false;
    }

    const rect = card.getBoundingClientRect();
    return (
      clientX >= rect.left &&
      clientX <= rect.right &&
      clientY >= rect.top &&
      clientY <= rect.bottom
    );
  }) || null;
}

function bindChartDragDrop() {
  const finishChartDrag = (event) => {
    if (!chartDragState || event.pointerId !== chartDragState.pointerId) {
      return;
    }

    const { symbol, card, dragging, overSymbol } = chartDragState;

    if (card.hasPointerCapture(event.pointerId)) {
      card.releasePointerCapture(event.pointerId);
    }

    card.classList.remove("is-dragging");
    chartsGrid.querySelectorAll(".chart-card.is-drag-over").forEach((element) => {
      element.classList.remove("is-drag-over");
    });

    if (dragging) {
      if (overSymbol && reorderWatchlist(symbol, overSymbol)) {
        renderWatchlist();
        rerenderChartsFromCache();
      }
    } else {
      selectSymbol(symbol, "detail");
    }

    chartDragState = null;
  };

  chartsGrid.addEventListener("pointerdown", (event) => {
    const card = event.target.closest(".chart-card");
    if (!card || event.button !== 0) {
      return;
    }

    chartDragState = {
      symbol: card.dataset.symbol,
      card,
      pointerId: event.pointerId,
      startX: event.clientX,
      startY: event.clientY,
      dragging: false,
      overSymbol: null,
    };

    card.setPointerCapture(event.pointerId);
  });

  chartsGrid.addEventListener("pointermove", (event) => {
    if (!chartDragState || event.pointerId !== chartDragState.pointerId) {
      return;
    }

    const distance = Math.hypot(
      event.clientX - chartDragState.startX,
      event.clientY - chartDragState.startY
    );

    if (!chartDragState.dragging && distance >= CHART_DRAG_THRESHOLD) {
      chartDragState.dragging = true;
      chartDragState.card.classList.add("is-dragging");
    }

    if (!chartDragState.dragging) {
      return;
    }

    event.preventDefault();

    const target = findChartDropTarget(
      event.clientX,
      event.clientY,
      chartDragState.card
    );

    chartsGrid.querySelectorAll(".chart-card.is-drag-over").forEach((element) => {
      element.classList.remove("is-drag-over");
    });

    if (target) {
      target.classList.add("is-drag-over");
      chartDragState.overSymbol = target.dataset.symbol;
    } else {
      chartDragState.overSymbol = null;
    }
  });

  chartsGrid.addEventListener("pointerup", finishChartDrag);
  chartsGrid.addEventListener("pointercancel", finishChartDrag);
}

function resizePriceChart() {
  if (priceChart) {
    priceChart.resize();
  }
}

function waitForNextFrame() {
  return new Promise((resolve) => {
    requestAnimationFrame(() => {
      requestAnimationFrame(resolve);
    });
  });
}

function chartIdForSymbol(symbol) {
  return `chart-${symbol.replace(/[^a-zA-Z0-9]+/g, "-")}`;
}

function quoteDigits(quote) {
  return quote?.instrument_type === "yield" ? 3 : 2;
}

function formatQuoteValue(quote, value, digits) {
  const resolvedDigits = digits ?? quoteDigits(quote);
  const formatted = formatNumber(value, resolvedDigits);
  if (quote?.unit === "%") {
    return `${formatted}%`;
  }
  if (quote?.unit && quote.unit !== quote.currency) {
    return `${formatted} ${quote.unit}`;
  }
  if (quote?.currency) {
    return `${formatted} ${quote.currency}`;
  }
  return formatted;
}

function formatQuotePrice(quote) {
  return formatQuoteValue(quote, quote.price);
}

function formatQuoteChange(quote, value) {
  const sign = value > 0 ? "+" : "";
  const formatted = formatNumber(value, quoteDigits(quote));
  if (quote?.unit === "%") {
    return `${sign}${formatted}%`;
  }
  return `${sign}${formatted}`;
}

function formatNumber(value, digits = 2) {
  if (value === null || value === undefined || Number.isNaN(value)) {
    return "—";
  }
  return Number(value).toLocaleString(undefined, {
    minimumFractionDigits: digits,
    maximumFractionDigits: digits,
  });
}

function formatVolume(value) {
  if (value === null || value === undefined) {
    return "—";
  }
  if (value >= 1_000_000_000) {
    return `${(value / 1_000_000_000).toFixed(2)}B`;
  }
  if (value >= 1_000_000) {
    return `${(value / 1_000_000).toFixed(2)}M`;
  }
  if (value >= 1_000) {
    return `${(value / 1_000).toFixed(2)}K`;
  }
  return String(value);
}

function formatMarketCap(value) {
  if (value === null || value === undefined) {
    return "—";
  }
  if (value >= 1_000_000_000_000) {
    return `${(value / 1_000_000_000_000).toFixed(2)}T`;
  }
  if (value >= 1_000_000_000) {
    return `${(value / 1_000_000_000).toFixed(2)}B`;
  }
  if (value >= 1_000_000) {
    return `${(value / 1_000_000).toFixed(2)}M`;
  }
  return String(value);
}

function changeClass(value) {
  if (value > 0) {
    return "up";
  }
  if (value < 0) {
    return "down";
  }
  return "flat";
}

function formatChange(change, percent) {
  const sign = change > 0 ? "+" : "";
  return `${sign}${formatNumber(change)} (${sign}${formatNumber(percent)}%)`;
}

function formatSigned(value, suffix = "") {
  if (value === null || value === undefined || Number.isNaN(value)) {
    return "—";
  }
  const sign = value > 0 ? "+" : "";
  return `${sign}${formatNumber(value)}${suffix}`;
}

function syncPeriodTabs() {
  [periodTabs, chartsPeriodTabs].forEach((tabs) => {
    tabs.querySelectorAll("button").forEach((button) => {
      button.classList.toggle("active", button.dataset.period === currentPeriod);
    });
  });
}

async function fetchQuotes(symbols) {
  const response = await fetch("/api/quotes", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ symbols }),
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.error || "無法取得報價");
  }
  return data;
}

async function fetchQuote(symbol) {
  const data = await fetchQuotes([symbol]);
  if (data.errors?.length) {
    throw new Error(data.errors[0].error);
  }
  const quote = data.quotes[0];
  quoteCache[symbol] = quote;
  return quote;
}

async function fetchHistory(symbol, period) {
  const cacheKey = `${symbol}-${period}`;
  if (historyCache[cacheKey]) {
    return historyCache[cacheKey];
  }

  const response = await fetch(
    `/api/history/${encodeURIComponent(symbol)}?period=${encodeURIComponent(period)}`
  );
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.error || "無法取得歷史資料");
  }

  historyCache[cacheKey] = data;
  return data;
}

async function fetchHistories(symbols, period) {
  const response = await fetch("/api/histories", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ symbols, period }),
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.error || "無法取得歷史資料");
  }

  data.histories.forEach((history) => {
    historyCache[`${history.symbol}-${period}`] = history;
  });

  return data;
}

function getSortedQuotes() {
  const quotes = watchlist
    .map((symbol) => quoteCache[symbol])
    .filter(Boolean);

  quotes.sort((left, right) => {
    const leftValue = left[sortKey];
    const rightValue = right[sortKey];

    if (typeof leftValue === "number" && typeof rightValue === "number") {
      return sortAsc ? leftValue - rightValue : rightValue - leftValue;
    }

    const leftText = String(leftValue ?? "").toLowerCase();
    const rightText = String(rightValue ?? "").toLowerCase();
    if (leftText < rightText) {
      return sortAsc ? -1 : 1;
    }
    if (leftText > rightText) {
      return sortAsc ? 1 : -1;
    }
    return 0;
  });

  return quotes;
}

function resetChartsPanelLayout() {
  chartsPanel.classList.remove("is-dense", "is-fit-screen");
  chartsGrid.classList.remove("is-dense", "is-fit-screen");
  chartsGrid.style.gridTemplateColumns = "";
  chartsGrid.style.gridTemplateRows = "";
  updateContentFitMode(false);
}

function updatePanelsVisibility() {
  const hasStocks = watchlist.length > 0;

  emptyState.hidden = hasStocks;
  overviewPanel.hidden = !hasStocks || currentView !== "overview";
  chartsPanel.hidden = !hasStocks || currentView !== "charts";
  detailPanel.hidden = !hasStocks || currentView !== "detail";

  if (currentView !== "charts") {
    resetChartsPanelLayout();
  } else if (!chartsPanel.hidden) {
    const visibleCount = getVisibleChartSymbols().length;
    updateContentFitMode(shouldUseFitScreenLayout(visibleCount));
  }

  viewTabs.querySelectorAll("button").forEach((button) => {
    button.classList.toggle("active", button.dataset.view === currentView);
  });
}

function resizeMiniCharts() {
  requestAnimationFrame(() => {
    Object.values(miniCharts).forEach((chart) => chart.resize());
  });
}

function sampleHistoryForChart(history, maxPoints = 120) {
  if (history.prices.length <= maxPoints) {
    return history;
  }

  const step = Math.ceil(history.prices.length / maxPoints);
  const labels = [];
  const prices = [];

  for (let index = 0; index < history.prices.length; index += step) {
    labels.push(history.labels[index]);
    prices.push(history.prices[index]);
  }

  const lastIndex = history.prices.length - 1;
  if (labels[labels.length - 1] !== history.labels[lastIndex]) {
    labels.push(history.labels[lastIndex]);
    prices.push(history.prices[lastIndex]);
  }

  const startPrice = prices[0];
  const endPrice = prices[prices.length - 1];
  const trendChange = endPrice - startPrice;
  const trendPercent = startPrice ? (trendChange / startPrice) * 100 : 0;

  return {
    ...history,
    labels,
    prices,
    start_price: startPrice,
    end_price: endPrice,
    trend_change: trendChange,
    trend_percent: trendPercent,
  };
}

function destroyMiniCharts() {
  Object.values(miniCharts).forEach((chart) => chart.destroy());
  miniCharts = {};
}

function createMiniChart(canvas, history) {
  const chartHistory = sampleHistoryForChart(history);
  const lineColor = chartHistory.trend_change >= 0 ? "#4ade80" : "#f87171";
  const fillColor = chartHistory.trend_change >= 0
    ? "rgba(74, 222, 128, 0.15)"
    : "rgba(248, 113, 113, 0.15)";

  return new Chart(canvas, {
    type: "line",
    data: {
      labels: chartHistory.labels,
      datasets: [
        {
          data: chartHistory.prices,
          borderColor: lineColor,
          backgroundColor: fillColor,
          fill: true,
          tension: 0.3,
          pointRadius: 0,
          borderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          mode: "index",
          intersect: false,
        },
      },
      scales: {
        x: {
          display: false,
        },
        y: {
          display: false,
        },
      },
    },
  });
}

function renderOverview() {
  const quotes = getSortedQuotes();
  let upCount = 0;
  let downCount = 0;
  let flatCount = 0;

  overviewBody.innerHTML = "";

  quotes.forEach((quote) => {
    if (quote.change > 0) {
      upCount += 1;
    } else if (quote.change < 0) {
      downCount += 1;
    } else {
      flatCount += 1;
    }

    const row = document.createElement("tr");
    row.className = quote.symbol === selectedSymbol ? "active" : "";
    row.innerHTML = `
      <td class="symbol-cell">${quote.symbol}</td>
      <td class="name-cell" title="${quote.name}">${quote.name}</td>
      <td class="num-cell">${formatQuotePrice(quote)}</td>
      <td class="num-cell ${changeClass(quote.change)}">${formatQuoteChange(quote, quote.change)}</td>
      <td class="num-cell ${changeClass(quote.change)}">${formatSigned(quote.change_percent, "%")}</td>
      <td class="num-cell">${formatNumber(quote.day_high)}</td>
      <td class="num-cell">${formatNumber(quote.day_low)}</td>
      <td class="num-cell">${formatVolume(quote.volume)}</td>
    `;

    row.addEventListener("click", () => {
      selectSymbol(quote.symbol, "detail");
    });

    overviewBody.appendChild(row);
  });

  summaryCount.textContent = String(watchlist.length);
  summaryUp.textContent = String(upCount);
  summaryDown.textContent = String(downCount);
  summaryFlat.textContent = String(flatCount);

  if (quotes.length > 0) {
    overviewUpdated.textContent = `最後更新：${quotes[0].updated_at}`;
  } else {
    overviewUpdated.textContent = "";
  }

  document.querySelectorAll(".overview-table th").forEach((header) => {
    const key = header.dataset.sort;
    header.classList.toggle("sorted", key === sortKey);
    const arrow = key === sortKey ? (sortAsc ? " ▲" : " ▼") : "";
    header.textContent = `${COLUMN_LABELS[key]}${arrow}`;
  });
}

function renderChartsGrid(histories) {
  destroyMiniCharts();
  chartsGrid.innerHTML = "";

  const historyMap = Object.fromEntries(histories.map((item) => [item.symbol, item]));
  const visibleSymbols = getVisibleChartSymbols();

  applyChartsGridLayout(visibleSymbols.length);
  updateChartsPagination();

  visibleSymbols.forEach((symbol) => {
    const quote = quoteCache[symbol];
    const history = historyMap[symbol];
    if (!quote || !history) {
      return;
    }

    const card = document.createElement("article");
    card.className = `chart-card${symbol === selectedSymbol ? " active" : ""}`;
    card.dataset.symbol = symbol;

    const canvasId = chartIdForSymbol(symbol);
    card.innerHTML = `
      <header class="chart-card-header">
        <div class="chart-card-title">
          <p class="chart-card-symbol">${quote.symbol}</p>
          <h3 class="chart-card-name">${quote.name}</h3>
        </div>
        <div class="chart-card-quote">
          <strong class="chart-card-price">${formatQuotePrice(quote)}</strong>
          <span class="chart-card-change ${changeClass(quote.change)}">${formatSigned(quote.change_percent, "%")}</span>
          <span class="chart-card-trend">區間 ${formatSigned(history.trend_percent, "%")}</span>
        </div>
      </header>
      <div class="mini-chart-wrap">
        <canvas id="${canvasId}"></canvas>
      </div>
    `;

    chartsGrid.appendChild(card);

    const canvas = document.getElementById(canvasId);
    miniCharts[symbol] = createMiniChart(canvas, history);
  });

  if (histories.length > 0 && quoteCache[visibleSymbols[0]]) {
    overviewUpdated.textContent = `最後更新：${quoteCache[visibleSymbols[0]].updated_at}`;
  }

  resizeMiniCharts();
}

function rerenderChartsFromCache() {
  if (lastChartHistories.length > 0) {
    renderChartsGrid(lastChartHistories);
  }
}

async function loadCharts() {
  if (watchlist.length === 0) {
    destroyMiniCharts();
    chartsGrid.innerHTML = "";
    return;
  }

  const symbols = getVisibleChartSymbols();
  const data = await fetchHistories(symbols, currentPeriod);

  if (data.errors?.length) {
    console.warn(data.errors.map((item) => `${item.symbol}: ${item.error}`).join("\n"));
  }

  if (data.histories.length === 0) {
    const message = data.errors?.length
      ? data.errors.map((item) => `${item.symbol}: ${item.error}`).join("\n")
      : "無法取得走勢資料";
    throw new Error(message);
  }

  lastChartHistories = data.histories;
  renderChartsGrid(lastChartHistories);
}

function renderWatchlist() {
  watchlistEl.innerHTML = "";

  watchlist.forEach((symbol) => {
    const quote = quoteCache[symbol];
    const item = document.createElement("li");
    item.className = `watch-item${symbol === selectedSymbol ? " active" : ""}`;

    const main = document.createElement("div");
    main.className = "watch-item-main";

    const symbolEl = document.createElement("div");
    symbolEl.className = "watch-item-symbol";
    symbolEl.textContent = symbol;

    const nameEl = document.createElement("div");
    nameEl.className = "watch-item-name";
    nameEl.textContent = quote?.name || "載入中...";

    main.appendChild(symbolEl);
    main.appendChild(nameEl);

    const quoteEl = document.createElement("div");
    quoteEl.className = "watch-item-quote";

    const priceEl = document.createElement("div");
    priceEl.className = "watch-item-price";
    priceEl.textContent = quote ? formatQuotePrice(quote) : "—";

    const changeEl = document.createElement("div");
    changeEl.className = `watch-item-change ${quote ? changeClass(quote.change) : "flat"}`;
    changeEl.textContent = quote
      ? `${quote.change > 0 ? "+" : ""}${formatNumber(quote.change_percent)}%`
      : "—";

    quoteEl.appendChild(priceEl);
    quoteEl.appendChild(changeEl);

    const removeBtn = document.createElement("button");
    removeBtn.type = "button";
    removeBtn.className = "remove-btn";
    removeBtn.textContent = "移除";
    removeBtn.addEventListener("click", (event) => {
      event.stopPropagation();
      removeSymbol(symbol);
    });

    item.addEventListener("click", () => selectSymbol(symbol, "detail"));
    item.appendChild(main);
    item.appendChild(quoteEl);
    item.appendChild(removeBtn);
    watchlistEl.appendChild(item);
  });
}

function renderQuote(quote) {
  const labels = STAT_LABELS[quote.instrument_type] || STAT_LABELS.stock;
  const isYield = quote.instrument_type === "yield";

  detailSymbol.textContent = quote.symbol;
  detailName.textContent = quote.name;
  detailPrice.textContent = formatNumber(quote.price, quoteDigits(quote));
  detailCurrency.textContent = isYield ? "%" : (quote.currency || quote.unit || "");
  detailChange.textContent = `${formatQuoteChange(quote, quote.change)} (${formatSigned(quote.change_percent)}%)`;
  detailChange.className = `change ${changeClass(quote.change)}`;
  detailUpdated.textContent = `${quote.price_label} · 更新時間：${quote.updated_at}`;

  statPrevLabel.textContent = labels.prev;
  statHighLabel.textContent = labels.high;
  statLowLabel.textContent = labels.low;
  stat52HighLabel.textContent = labels.week52High;
  stat52LowLabel.textContent = labels.week52Low;

  statPrevClose.textContent = formatQuoteValue(quote, quote.previous_close);
  statDayHigh.textContent = formatQuoteValue(quote, quote.day_high);
  statDayLow.textContent = formatQuoteValue(quote, quote.day_low);
  statVolume.textContent = formatVolume(quote.volume);
  stat52High.textContent = formatQuoteValue(quote, quote.fifty_two_week_high);
  stat52Low.textContent = formatQuoteValue(quote, quote.fifty_two_week_low);
  statMarketCap.textContent = formatMarketCap(quote.market_cap);

  statVolumeCard.hidden = isYield;
  statMarketCapCard.hidden = isYield || quote.instrument_type === "bond_etf";
}

function updateHistoryStats(history) {
  const quote = quoteCache[history.symbol];
  trendChange.textContent = formatChange(history.trend_change, history.trend_percent);
  trendChange.className = changeClass(history.trend_change);
  trendPercent.textContent = `${history.trend_percent > 0 ? "+" : ""}${formatNumber(history.trend_percent)}%`;
  trendPercent.className = changeClass(history.trend_change);
  trendStart.textContent = quote
    ? formatQuoteValue(quote, history.start_price)
    : formatNumber(history.start_price);
  trendEnd.textContent = quote
    ? formatQuoteValue(quote, history.end_price)
    : formatNumber(history.end_price);
}

function buildPriceChart(history) {
  const canvas = document.getElementById("price-chart");
  if (!canvas) {
    return null;
  }

  const lineColor = history.trend_change >= 0 ? "#4ade80" : "#f87171";
  const fillColor = history.trend_change >= 0
    ? "rgba(74, 222, 128, 0.12)"
    : "rgba(248, 113, 113, 0.12)";

  return new Chart(canvas, {
    type: "line",
    data: {
      labels: history.labels,
      datasets: [
        {
          label: "收盤價",
          data: history.prices,
          borderColor: lineColor,
          backgroundColor: fillColor,
          fill: true,
          tension: 0.25,
          pointRadius: 0,
          borderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      aspectRatio: 2.4,
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          mode: "index",
          intersect: false,
        },
      },
      scales: {
        x: {
          ticks: {
            color: "#94a3b8",
            maxTicksLimit: 8,
          },
          grid: {
            color: "rgba(148, 163, 184, 0.08)",
          },
        },
        y: {
          ticks: {
            color: "#94a3b8",
          },
          grid: {
            color: "rgba(148, 163, 184, 0.08)",
          },
        },
      },
    },
  });
}

async function renderDetailHistory(history) {
  updateHistoryStats(history);

  if (priceChart) {
    priceChart.destroy();
    priceChart = null;
  }

  if (detailPanel.hidden) {
    return;
  }

  await waitForNextFrame();
  priceChart = buildPriceChart(history);
  resizePriceChart();
}

async function finishDetailPanelUpdate() {
  if (currentView !== "detail" || detailPanel.hidden) {
    return;
  }

  await waitForNextFrame();
  resizePriceChart();
}

async function loadDetail(symbol) {
  const quote = quoteCache[symbol] || await fetchQuote(symbol);
  renderQuote(quote);

  const history = await fetchHistory(symbol, currentPeriod);
  await renderDetailHistory(history);
}

function getActivePanel() {
  if (currentView === "overview") {
    return overviewPanel;
  }
  if (currentView === "charts") {
    return chartsPanel;
  }
  return detailPanel;
}

async function setView(view) {
  currentView = view;
  if (currentView === "detail") {
    ensureSelectedSymbol();
    renderWatchlist();
  }
  updatePanelsVisibility();

  const panel = getActivePanel();
  panel.classList.add("loading");

  try {
    if (currentView === "overview") {
      renderOverview();
    } else if (currentView === "charts") {
      await loadCharts();
    } else if (selectedSymbol) {
      await loadDetail(selectedSymbol);
    }
  } catch (error) {
    alert(error.message);
  } finally {
    panel.classList.remove("loading");
    await finishDetailPanelUpdate();
  }
}

async function selectSymbol(symbol, view = currentView) {
  selectedSymbol = symbol;
  currentView = view;
  renderWatchlist();
  updatePanelsVisibility();

  const panel = getActivePanel();
  panel.classList.add("loading");

  try {
    if (currentView === "detail") {
      await loadDetail(symbol);
    } else if (currentView === "charts") {
      await loadCharts();
    } else {
      renderOverview();
    }
  } catch (error) {
    alert(error.message);
  } finally {
    panel.classList.remove("loading");
    await finishDetailPanelUpdate();
  }
}

async function changePeriod(period) {
  currentPeriod = period;
  syncPeriodTabs();
  historyCache = {};

  const panel = getActivePanel();
  panel.classList.add("loading");

  try {
    if (currentView === "detail" && selectedSymbol) {
      const history = await fetchHistory(selectedSymbol, currentPeriod);
      await renderDetailHistory(history);
    } else if (currentView === "charts") {
      await loadCharts();
    }
  } catch (error) {
    alert(error.message);
  } finally {
    panel.classList.remove("loading");
    await finishDetailPanelUpdate();
  }
}

async function refreshAll() {
  if (watchlist.length === 0) {
    updatePanelsVisibility();
    return;
  }

  refreshAllBtn.disabled = true;
  overviewPanel.classList.add("loading");
  chartsPanel.classList.add("loading");
  detailPanel.classList.add("loading");
  historyCache = {};

  try {
    const data = await fetchQuotes(watchlist);

    data.quotes.forEach((quote) => {
      quoteCache[quote.symbol] = quote;
    });

    if (data.errors?.length) {
      const failed = data.errors.map((item) => `${item.symbol}: ${item.error}`).join("\n");
      console.warn(failed);
    }

    renderWatchlist();
    renderOverview();
    updatePanelsVisibility();

    if (currentView === "charts") {
      await loadCharts();
    } else if (currentView === "detail" && selectedSymbol) {
      await loadDetail(selectedSymbol);
    }
  } catch (error) {
    alert(error.message);
  } finally {
    refreshAllBtn.disabled = false;
    overviewPanel.classList.remove("loading");
    chartsPanel.classList.remove("loading");
    detailPanel.classList.remove("loading");
    await finishDetailPanelUpdate();
  }
}

function addSymbol(rawSymbol) {
  const symbol = rawSymbol.trim().toUpperCase();
  if (!symbol) {
    alert("請輸入股票代號");
    return;
  }

  if (!watchlist.includes(symbol)) {
    watchlist.unshift(symbol);
    saveWatchlist();
  }

  symbolInput.value = "";
  refreshAll();
}

function removeSymbol(symbol) {
  watchlist = watchlist.filter((item) => item !== symbol);
  saveWatchlist();
  delete quoteCache[symbol];

  Object.keys(historyCache).forEach((key) => {
    if (key.startsWith(`${symbol}-`)) {
      delete historyCache[key];
    }
  });

  if (miniCharts[symbol]) {
    miniCharts[symbol].destroy();
    delete miniCharts[symbol];
  }

  if (selectedSymbol === symbol) {
    selectedSymbol = watchlist[0] || null;
  }

  if (watchlist.length === 0) {
    destroyMiniCharts();
    chartsGrid.innerHTML = "";
    chartsPagination.hidden = true;
    lastChartHistories = [];
    currentView = "overview";
    updatePanelsVisibility();
    renderWatchlist();
    return;
  }

  refreshAll();
}

addForm.addEventListener("submit", (event) => {
  event.preventDefault();
  addSymbol(symbolInput.value);
});

refreshAllBtn.addEventListener("click", refreshAll);

viewTabs.addEventListener("click", (event) => {
  const button = event.target.closest("button[data-view]");
  if (!button) {
    return;
  }

  if (button.dataset.view === currentView) {
    return;
  }

  setView(button.dataset.view);
});

document.querySelector(".overview-table thead").addEventListener("click", (event) => {
  const header = event.target.closest("th[data-sort]");
  if (!header) {
    return;
  }

  const key = header.dataset.sort;
  if (sortKey === key) {
    sortAsc = !sortAsc;
  } else {
    sortKey = key;
    sortAsc = key === "symbol" || key === "name";
  }

  renderOverview();
});

function bindPeriodTabs(tabs) {
  tabs.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-period]");
    if (!button || button.dataset.period === currentPeriod) {
      return;
    }

    changePeriod(button.dataset.period);
  });
}

bindPeriodTabs(periodTabs);
bindPeriodTabs(chartsPeriodTabs);

chartDisplayCountSelect.addEventListener("change", () => {
  chartDisplayCount = chartDisplayCountSelect.value === "all"
    ? "all"
    : Number(chartDisplayCountSelect.value);
  chartPageIndex = 0;
  saveChartDisplayCount();
  rerenderChartsFromCache();
});

chartsPrevBtn.addEventListener("click", () => {
  if (chartPageIndex > 0) {
    chartPageIndex -= 1;
    rerenderChartsFromCache();
  }
});

chartsNextBtn.addEventListener("click", () => {
  if (chartPageIndex < getTotalChartPages() - 1) {
    chartPageIndex += 1;
    rerenderChartsFromCache();
  }
});

async function init() {
  saveWatchlist();
  syncPeriodTabs();
  syncChartDisplayControls();
  bindChartDragDrop();
  renderWatchlist();
  updatePanelsVisibility();

  window.addEventListener("resize", () => {
    resizeMiniCharts();
    resizePriceChart();
  });

  try {
    await refreshAll();
  } catch (error) {
    alert(error.message);
  }
}

init();
