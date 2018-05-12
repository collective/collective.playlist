define([
  'jquery',
  'pat-base',
  'pat-registry',
], function($, Base, registry) {
  'use strict';

  var Pattern = Base.extend({
    name: 'pat-collectiveplaylist',
    trigger: '#jquery_jplayer_playlist',
    parser: 'mockup',
    defaults: {
    },
    init: function() {
        // pjax
        $("body").append($("#playerfooterviewlet"));
        
        $(document).pjax('div.outer-wrapper a', 'div.outer-wrapper', {
            fragment:'div.outer-wrapper', 
            timeout: 5000
            });
        
        $('div.outer-wrapper').on('pjax:success', function () {
            $.pjax({ // TODO apply toolbar pattern: ? ajax_load=1
                url: window.location.href,
                container: '#edit-zone',
                fragment: '#edit-zone',
                push: false,
                timeout: 5000
            });
        });
        $('#edit-zone').on('pjax:success', function () {
            // TODO apply toolbar pattern
            registry.scan($('#edit-zone'));
            // if (registry.initialized) {
            //     registry.scan(document.body, [name]);
            // }
        });
        
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
