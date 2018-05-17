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
        
        var pjax = new P({
            elements: ["div.outer-wrapper a"],
            selectors: ["#edit-zone", "div.outer-wrapper"],
            cacheBust: false
        });

        // update css body classes
        var bodyclass = ""
        pjax._handleResponse = pjax.handleResponse;
        pjax.handleResponse = function(responseText, request, href) {
            try {
                var mt = responseText.match(/body.*? class="(.*?)"/);
                if (mt) {
                    bodyclass = mt[1];
                }                
            } catch(err) {
                console.error(err);
            }
            pjax._handleResponse(responseText, request, href);
        }
        
        document.addEventListener("pjax:success", function() {
            $("body").attr("class", bodyclass);
            // apply patterns
            registry.scan(document.body);
        });
        
        
        // JPlayer
        var tracks = $('#jquery_jplayer_playlist').attr('data-tracks');
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
