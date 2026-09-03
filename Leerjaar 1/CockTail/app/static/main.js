window.addEventListener("load", function () {

    const element = document.querySelectorAll('.cocktail')
    element.forEach(function(el){
        el.addEventListener('click', function () {
            event.preventDefault();
            
            let id = this.id;
            localStorage.setItem('previousurl', window.location.href)

            const urlParams = new URLSearchParams();
            urlParams.set('query', id);

            window.location.href = '/info?' + urlParams.toString();
        });
    });

    document.querySelector('#back').addEventListener('click', function (){
        window.location.href = localStorage.getItem('previousurl');
    });

});
