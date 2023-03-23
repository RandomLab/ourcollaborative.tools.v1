<script setup>

    import { ref, onMounted } from 'vue'

    import { useRouter, useRoute } from 'vue-router'

    import { storeToRefs } from 'pinia'
    import { useImagesStore } from '../store/images'

    const router = useRouter()

    const { images, loading, error } = storeToRefs(useImagesStore())
    const { fetchImages } = useImagesStore()

    fetchImages()

    const index = ref(null)

    function gotoProject(path) {
        router.push(path)
    }

    function calcWidth() {
        const indexWidth = index.value.offsetWidth
        const imageWidth = indexWidth / 4
        return `width: ${imageWidth}px`
    }

    function randomizeImagesIndex(images) {
        for (let i = images.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i+1))
            const tmp = images[i]
            images[i] = images[j]
            images[j] = tmp
        }
        return images
    }

</script>


<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>

        <div 
            v-if="images" 
            class="index"
            ref="index"
        >

            <div 
                class="item"
                v-for="image in images"
                :key="image.id"
            >
                    
                <img
                    @click="gotoProject(`/project/${image.project.slug}`)"
                    :src="image.image" 
                />

            </div>
        
        </div>
    </main>
</template>


