$(document).ready(() => {
    $("#user-menu-button").click((e) => {
        e.preventDefault();
        e.stopPropagation();
        $("#dropdown").toggleClass("hidden")

        // Hide on outside click
        $(document).one('click', closeMenu = (e) => {
            if($('#dropdown').has(e.target).length === 0){
                $('#dropdown').addClass('hidden');
            } else {
                $(document).one('click', closeMenu);
            }
        });
    })

})

