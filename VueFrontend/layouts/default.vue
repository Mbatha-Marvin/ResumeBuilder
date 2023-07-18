<template>
   <div>
    <section size="A4">
    <main class="main">
        <slot />
    </main>
    </section>
   </div>

</template>

<script setup>

</script>

<style scoped>

section {
    background: white !important;
    display: block !important;
    margin: 0 auto !important;
    margin-bottom: 0.5cm !important;
    margin-top: 5px !important;
    width: auto !important;
    /* box-shadow: 0 0 0.5cm rgba(0, 0, 0, 0.5); */
}

section[size="A4"] {
    width: 21cm !important;
    height: 29.7cm !important;
}

@media print {
    section {
        margin: 0 !important;
        box-shadow: 0 !important;
    }
}

.main {
    /* margin-left: 3px !important; */
    padding: 3px !important;
}
</style>