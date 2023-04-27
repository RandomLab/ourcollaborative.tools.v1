<script setup>

    import { storeToRefs } from 'pinia'
    
    import { useImagesStore } from '../../store/images'
    
    const props = defineProps(['id'])
    
    const { images, loading, error } = storeToRefs(useImagesStore())
    
    const { fetchImagesProject } = useImagesStore()

    fetchImagesProject(props.id)

</script>

<template>
    <div class="loading" v-if="loading">Loading post...</div>
    <div class="error" v-if="error">{{ error.message }}</div>
    <ol 
        v-if="images"
        class="project-informations--images">
            <li
                v-for="image in images"
                :key="image.id"
            >
                <div class="ref">image</div>
                <img :src="image.image" />
                <figcaption>{{ image.legend }}</figcaption>

            </li>
    </ol>
</template>