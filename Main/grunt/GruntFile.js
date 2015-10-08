module.exports = function(grunt) {

    grunt.initConfig({
        responsive_images: {
            myTask: {
                options: {
                    engine: 'im',
                    sizes: [{
                        width: '20%',
                        height: '20%',
                        rename: false
                    }]
                },
                files: [{
                    expand: true,
                    cwd: '../public/images/src/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: '../public/images/dist/'
                }]
            }
        },
        imagemin: {
            dynamic: {
                options: {
                    optimizationLevel: 7
                },
                files: [{
                    expand: true,
                    cwd: '../public/images/dist/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: '../public/images/dist/'
                }]
            }
        }
    });

    grunt.loadNpmTasks('grunt-responsive-images');
    grunt.loadNpmTasks('grunt-contrib-imagemin');

    grunt.registerTask('default', ['responsive_images','imagemin']);

};