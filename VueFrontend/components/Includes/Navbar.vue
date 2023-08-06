<template>
  <nav class="navbar sticky-top navbar-expand-lg bg-success shadow">
    <div class="container">
      <NuxtLink class="navbar-brand" :to="'/'">
        <img src="/assets/img/svg/bootstrap.svg" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
        ResumeBuilder
      </NuxtLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <NuxtLink class="nav-link text-dark" :to="'/'">Home</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink class="nav-link text-dark" :to="'/resume/template'">Templates</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink class="nav-link text-dark" :to="'/resume/create'">Free Trial</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink class="nav-link text-dark" :to="'/template'">MainTemplate</NuxtLink>
          </li>
          <li class="nav-item d-grid gap-2 d-md-flex">
              <NuxtLink class="btn btn-primary me-md-2 text-dark" :to="'/auth/register'">Register</NuxtLink>
              <NuxtLink class="btn btn-danger me-md-2 text-dark" :to="'/auth/login'">Login</NuxtLink>
          </li>

        </ul>

      </div>
    </div>
  </nav>
</template>
  
<script>
export default {
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>
  
<style>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #333;
  color: #fff;
}

.navbar-logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.navbar-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
}

.navbar-icon {
  display: block;
  width: 20px;
  height: 2px;
  background-color: #fff;
  position: relative;
}

.navbar-icon::before,
.navbar-icon::after {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: #fff;
}

.navbar-icon::before {
  top: -7px;
}

.navbar-icon::after {
  top: 7px;
}

.nav-link.active {
  font-weight: bold;
}

.navbar-menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.navbar-item {
  margin-left: 1rem;
}

/* Media Query for Mobile Navigation */
@media screen and (max-width: 768px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
  }

  .navbar-menu {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    background-color: #333;
    width: 100%;
  }

  .navbar-open .navbar-menu {
    display: flex;
  }

  .navbar-item {
    margin: 0;
    width: 100%;
  }

  .navbar-toggle {
    display: block;
  }
}
</style>
  