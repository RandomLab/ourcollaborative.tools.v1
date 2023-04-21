<script setup>
    
    const props = defineProps(['width', 'height'])

</script>

<template>
  <svg xmlns="http://www.w3.org/2000/svg"
    :width="width"
    :height="height"
    viewBox="0 0 50 50"
  >
        <line x1="50" y1="50" x2="0" y2="0"/>
        <line x1="0" y1="50" x2="50" y2="0"/>
  </svg>
</template>

<style scoped>

    line {
        stroke: var(--second-color);
        stroke-width: 1;
    }
    
</style>