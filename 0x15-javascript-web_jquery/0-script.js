const element = document.querySelector('header');

if (element !== null) {
    element.style.color = '#FF0000';
} else {
    console.error('Header element not found');
}
