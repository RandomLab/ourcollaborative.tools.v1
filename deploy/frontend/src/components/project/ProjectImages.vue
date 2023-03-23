<script setup>

    import { storeToRefs } from 'pinia'
    
    import { useImagesStore } from '../../store/images'
    
    const props = defineProps(['id'])
    
    const { images, loading, error } = storeToRefs(useImagesStore())
    
    const { fetchImagesProject } = useImagesStore()

    fetchImagesProject(props.id)

</script>

<template>
    <p v-if="loading">Loading post...</p>
    <p v-if="error">{{ error.message }}</p>
    <ol 
        v-if="images"
        class="project-informations--images">
            <li
                v-for="image in images"
                :key="image.id"
            >
                <div class="ref">image</div>
                <img :src="image.image" />
                <figcaption>{{ image.legende }}</figcaption>

            </li>
    </ol>
</template>