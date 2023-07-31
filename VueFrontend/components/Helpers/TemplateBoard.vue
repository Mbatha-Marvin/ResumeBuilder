<template lang="">
    <div :id="id" @dragover.prevent @drop.prevent="drop" class="board">
        <slot />
    </div>
</template>
<script>
export default {
   props: {
       id: {
           type: String,
           required: true
       }
   },
    methods: {
         drop(e) {
              const card_id = e.dataTransfer.getData('card_id')
              const card = document.getElementById(card_id)
              card.style.display = 'block'
              e.target.appendChild(card)
         }
    } 
}
</script>
<style lang="">
    
</style>