define([
  'jquery',
  'pat-base',
], function($, Base) {
  'use strict';

  var Pattern = Base.extend({
    name: 'pat-collectiveplaylist',
    trigger: '#jquery_jplayer_playlist',
    parser: 'mockup',
    defaults: {
    },
    init: function() {
            var tracks = $('#tracks').html();
            tracks = tracks.replace(/'/g, '"');
            tracks = JSON.parse(tracks);
        
            new jPlayerPlaylist({
              jPlayer: '#jquery_jplayer_playlist',
              cssSelectorAncestor: '#jp_container_playlist'
            }, tracks, {
              volume: 0.85,
              playlistOptions: {
                autoPlay: false,
                // displayTime: 0,
                // addTime: 0,
                // removeTime: 0,
                // shuffleTime: 0
              },
              swfPath: '/++plone++collective.playlist',
              solution: 'html, flash',
              supplied: 'mp3, oga, ogg, wav',
              wmode: 'window',
              useStateClassSkin: true,
              autoBlur: false,
              smoothPlayBar: true,
              keyEnabled: true,
              remainingDuration: true
            }); // new jPlayerPlaylist

      
    }
  });

  return Pattern;
});
