

document.addEventListener('DOMContentLoaded', function() {
    /* Having issues with webpage loading */

    const app = Vue.createApp({
        delimiters: ["[[", "]]"],
        data() {
            return {
                message: "Hello Vue!",
                page: null,
                currTab: "About Me" 
            };
        },
        computed: {},
        methods: {
            fetchData: function() {
                fetch('http://localhost:8000/gets/loadAboutMe/' + 'Wombo', {
                    method: 'GET'
                })
                .then(response => { response.json().then(res => this.page = res)})
                .catch(err => console.log(err));
            }
        },
        beforeMount() {
            this.fetchData()
        }
        }).mount("#homepage");














});

