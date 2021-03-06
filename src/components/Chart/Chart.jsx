import React from 'react';
import TradingViewWidget, { Themes, BarStyles } from 'react-tradingview-widget';

// https://github.com/rafaelklaessen/react-tradingview-widget

function StockChart(props) {

  return (
    <div>
      <TradingViewWidget 
        // symbol='NASDAQ:AAPL'
        symbol={`${props.ticker}`}
        theme={Themes.DARK}
        width='1000px'
        height='550px'
        // barstyle={BarStyles.HEIKIN_ASHI}
      />
    </div>
  );
};

export default StockChart

