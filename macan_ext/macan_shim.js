window.chrome = window.chrome || {};
chrome.runtime = {
  sendMessage: function(message) {
    if (window.shrineBridge) {
      window.shrineBridge.receiveMessage(JSON.stringify(message));
    }
  },
  onMessage: {
    listeners: [],
    addListener: function(fn) {
      this.listeners.push(fn);
    },
    dispatch: function(msg) {
      this.listeners.forEach(fn => fn(msg));
    }
  }
};
