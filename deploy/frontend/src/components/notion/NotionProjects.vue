<script setup>

    import { storeToRefs } from 'pinia'
    
    import { useProjetStore } from '../../store/projects'
    
    const props = defineProps(['id'])
    
    const { projects, loading, error } = storeToRefs(useProjetStore())
    
    const { fetchProjetsNotion } = useProjetStore()

    fetchProjetsNotion(props.id)

</script>

<template>
    
    {{ projects }}

</template>