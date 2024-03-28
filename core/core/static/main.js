


    
document.addEventListener('DOMContentLoaded', function() {
    const app = Vue.createApp({
        delimiters: ["[[", "]]"],
        data() {
            return {
            message: "Hello Vue!",
            };
        },
        computed: {},
        methods: {},
        }).mount("#app");
});