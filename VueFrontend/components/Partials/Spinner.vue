<template>
    <div v-if="items.length === 0" class="spinner-container">
        <div class="spinner"></div>
    </div>
    <div v-else>
        <slot />
    </div>
</template>

<script setup lang="ts">
defineProps({
    items: {
        type: Array as () => string[],
        required: true
    }
});
</script>

<style scoped>
.spinner-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 10;
}

.spinner {
    width: 40px;
    height: 40px;
    border: 5px solid #f3f3f3;
    border-top: 5px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
</style>