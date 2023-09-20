<template>
  <div>
    <header>
      <div class="logo-text">
        <img :src="logo" alt="logo" />
      </div>

      <img class="menu-toggle" :src="menuBar" alt="menu" />
    </header>
  </div>
</template>

<script setup>
import logo from '../../assets/userNavigation/icons/graduation-cap.png'
import menuBar from '../../assets/userNavigation/icons/menu.svg'
import Close from '../../assets/userNavigation/icons/close.svg'

// import { defineComponent, ref } from 'vue';
</script>

<style scoped></style>
