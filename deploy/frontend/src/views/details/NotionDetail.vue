<script setup>

    import { ref, reactive, computed, onMounted } from 'vue'

    import { storeToRefs } from 'pinia'
    import { useNotionStore } from '../../store/notions'

    import NotionProjects from '../../components/notion/NotionProjects.vue'
    
    const { notions, notion, loading, error } = storeToRefs(useNotionStore())

    const { fetchNotions, setNotion } = useNotionStore()

    onMounted(() => {
        fetchNotions()
        setNotion()
    })


    const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    function filterByLetter(notions, letter) {
        const filterNotion = notions.filter((item) => {
            return item.title.charAt(0).toLowerCase() === letter
        })
        return filterNotion
    }

</script>

<template>

    <main>
        
        <p v-if="loading">Loading post...</p>
        
        <p v-if="error">{{ error.message }}</p>
        
        <div class="notion--container">
            <div class="notion--left">
                <div 
                    v-for="(letter, index) in alphabet"
                    :key="index"
                >
                    <div 
                        v-if="filterByLetter(notions, letter).length"
                        class="lettrine">
                        {{ letter }}.
                    </div>

                    <div 
                        v-if="filterByLetter(notions, letter)" 
                        class="notion--list"
                    >
                        
                        <div 
                            
                            v-for="notion in filterByLetter(notions, letter)"
                            :key="notion.id"
                            class="notion--item"
                        >
                            <h2><router-link
                                @click="setNotion(notion)" 
                                :to="`${notion.slug}`">{{ notion.title }}</router-link></h2>

                        </div>

                    </div>

                </div>             
            </div>
            <div 
                class="notion--right"
            >

                <notion-projects></notion-projects>


            </div>
        </div>

    </main>

</template>

<style scoped>

.notion--list {
    flex-direction: column;
}

.notion--item {
    width: 100%;
}

</style>