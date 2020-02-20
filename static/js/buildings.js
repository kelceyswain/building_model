
var buildingVue = new Vue({
    delimiters: ['${', '}$'],
    el: '#starting',
    
    mounted: function() {
        this.getBuildings();
        console.log('here');
    },
    data: {
        buildings: [],
        loading: false,
        currentBuilding: {},
        message: null,
    },
    methods: {
        getBuildings: function() {
            this.loading = true;
            this.$http.get('api/buildings/')
                .then((response) => {
                    this.buildings = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getBuilding: function(id) {
            this.loading = true;
            this.$http.get('api/building/${id}')
                .then((response) => {
                    this.currentBuilding = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
    },
});
        
