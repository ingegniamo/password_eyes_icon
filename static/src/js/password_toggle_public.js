(function () {
    document.addEventListener("click", function (e) {
        var toggle = e.target.closest(".password-toggle");
        if (!toggle) return;

        e.preventDefault();
        e.stopPropagation();

        var container = toggle.closest(".field-password");
        if (!container) return;

        var input = container.querySelector("input");
        if (!input) return;

        if (input.type === "password") {
            input.type = "text";
            toggle.classList.remove("fa-eye-slash");
            toggle.classList.add("fa-eye");
        } else {
            input.type = "password";
            toggle.classList.remove("fa-eye");
            toggle.classList.add("fa-eye-slash");
        }
    });
})();
