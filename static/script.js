function toggleTheme() {
    const body = document.querySelector('body');
    body.classList.toggle('theme-dark');
    body.classList.toggle('theme-light');

    // Save the user's preference in localStorage
    const theme = body.classList.contains('theme-dark') ? 'dark' : 'light';
    localStorage.setItem('theme', theme);
}

// Check if the user has a theme preference and set the theme accordingly
const theme = localStorage.getItem('theme');
if (theme === 'dark') {
    toggleTheme();
}

