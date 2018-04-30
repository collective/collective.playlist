// TODO Pattern https://training.plone.org/5/javascript/exercises/5.html

define([
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
      that.$el.append(' <b>collective.playlist was here!</b>');
    }
  });

  return Pattern;
});
