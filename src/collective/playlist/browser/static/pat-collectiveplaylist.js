define([
  'jquery',
  'pat-base',
  'pat-registry',
  'pjaxscript',
  'jplayerscript',
  'jplayerplaylistscript'
], function($, Base, registry, P) {
  'use strict';

  var Pattern = Base.extend({
    name: 'pat-collectiveplaylist',
    trigger: '#jquery_jplayer_playlist',
    
    init: function() {
        var that = this;
        
        // pjax
        $("body").append($("#playerfooterviewlet"));
        
        function whenContainerReady() {
            registry.scan(document.body);
        };
        var pjax = new P({
          elements: "div.outer-wrapper a",
          selectors: ["#edit-zone", "div.outer-wrapper"]
        });        
        document.addEventListener("pjax:success", whenContainerReady);
        
        
        // JPlayer
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
