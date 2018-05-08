define('pat-collectiveplaylist',[
  'jquery',
  'pat-base',
], function($, Base) {
  'use strict';

  var Pattern = Base.extend({
    name: 'pat-collectiveplaylist',
    trigger: '.pat-collectiveplaylist',
    parser: 'mockup',
    defaults: {
    },
    init: function() {
      var that = this;
      // that.$el.append(' <b>collective.playlist was here!</b>');
    }
  });

  return Pattern;
});

require([
  'pat-collectiveplaylist'
], function() {
  'use strict';
});



define("/Users/ksuess/Plone/playlist/src/collective/playlist/browser/static/bundle-collectiveplaylist.js", function(){});

