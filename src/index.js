import "./styles.css";

const search = instantsearch({
  indexName: "Simon_test_wine",
  searchClient: algoliasearch("RSBCBF0EG8", "362a46f9db7603d913d9f4eea9a47fde")
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: "#searchbox"
  }),

  instantsearch.widgets.hits({
    container: "#hits",
    templates: {
      item: `
    <div>
    <div class="hit-left">
      <div class="display_image">
        <image src="{{img}}" >
        </div> 
    </div>
    
    <div class="hit-right">
      <div class="hit_name">
      \Winery: {{#helpers.highlight}}{ "attribute": "winery"}{{/helpers.highlight}}
      <p>\Designation: {{#helpers.highlight}}{ "attribute": "designation"}{{/helpers.highlight}}</p>
      <p>\Region: {{#helpers.highlight}}{ "attribute": "region_1"}{{/helpers.highlight}}</p>
      <p>\Cépage: {{#helpers.highlight}}{ "attribute": "variety"}{{/helpers.highlight}}</p>

      </div> 
      <div class="price">
      \Price: $ {{price}}
      </div>
    </div>
    </div>
      `
    }
  }),

  instantsearch.widgets.refinementList({
    container: "#variety-list",
    attribute: "variety",
    searchable: true,
    searchablePlaceholder: "Syrah, Merlot, ..",
    searchableIsAlwaysActive: true
  }),

  instantsearch.widgets.refinementList({
    container: "#country-list",
    attribute: "country"
  }),

  instantsearch.widgets.refinementList({
    container: "#tags-list",
    attribute: "tags",
    searchable: true,
    searchablePlaceholder: "Honey, Lemon, ..",
    searchableIsAlwaysActive: true
  }),

  instantsearch.widgets.rangeSlider({
    container: "#price_range",
    attribute: "price"
  }),

  instantsearch.widgets.geoSearch({
    container: "#maps",
    googleReference: window.google,
    mapOptions: {
      mapTypeId: window.google.maps.MapTypeId.MAP
    },

    builtInMarker: {
      createOptions(item) {
        return {
          title: item.winery
        };
      },
      events: {
        click({ event, item, marker, map }) {
          console.log(item);
        }
      }
    }
  })
]);

search.start();
