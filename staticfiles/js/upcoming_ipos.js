// Handle Update buttons
document.querySelectorAll('.action-btn').forEach((btn, index) => {
  btn.addEventListener('click', () => {
    alert(`Update IPO at row ${index + 1}`);
    // You can replace with: window.location.href = `/admin-panel/ipos/update/${ipoId}/`
  });
});

// Handle Trash icon
document.querySelectorAll('.fa-trash-alt').forEach((icon, index) => {
  icon.addEventListener('click', () => {
    const confirmDelete = confirm(`Are you sure you want to delete IPO at row ${index + 1}?`);
    if (confirmDelete) {
      alert("IPO deleted (link this to your Django backend)");
      // Later: send fetch request or redirect to /admin-panel/ipos/delete/<id>/
    }
  });
});

// Handle View icon
document.querySelectorAll('.fa-eye').forEach((icon, index) => {
  icon.addEventListener('click', () => {
    alert(`Viewing IPO details for row ${index + 1}`);
    // Later: redirect to view page or open modal
  });
});

// Handle Register IPO button
const registerBtn = document.querySelector('.register-ipo-btn');
if (registerBtn) {
  registerBtn.addEventListener('click', () => {
    window.location.href = '/admin-panel/ipos/register/';
  });
}

// Handle Sidebar Dashboard link
const dashboardLink = document.querySelector('.sidebar .menu ul li a');
if (dashboardLink) {
  dashboardLink.addEventListener('click', (e) => {
    e.preventDefault();
    window.location.href = "/admin-panel/dashboard/";
  });
}

// Handle pagination demo
document.querySelectorAll('.page-number').forEach((page) => {
  page.addEventListener('click', (e) => {
    e.preventDefault();
    document.querySelectorAll('.page-number').forEach((p) => p.classList.remove('active'));
    page.classList.add('active');
  });
});
