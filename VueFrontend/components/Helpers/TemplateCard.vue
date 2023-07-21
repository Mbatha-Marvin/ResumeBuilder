<template lang="">
    <div :id="id" class="card" :draggable="draggable" @dragstart="dragstart" @dragover.stop>
        <slot/>
    </div>
</template>
<script>
export default {
    props: {
        id: {
            type: String,
            required: true
        },
        draggable: {
            type: Boolean,
            default: true
        }
    },
    methods: {
        dragstart(e) {
            e.dataTransfer.setData('card_id', e.target.id)
            setTimeout(() => {
                e.target.style.display = 'none'
            }, 0)
        }
    }
}
</script>
<style lang="">
    
</style>