// requirements
var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var minifyCSS = require('gulp-minify-css');
var rename = require('gulp-rename');

gulp.task('styles', function() {
    gulp.src('./scss/main.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(concat('style.min.css'))
    .pipe(gulp.dest('./static/styles'))
})

gulp.task('js', function() {
    gulp.src('./js/**/*.js')
        // .pipe(minifyCSS())
        .pipe(concat('app-main.js'))
        .pipe(gulp.dest('./static/scripts'));
});


//Watch task
gulp.task('default',function() {
    gulp.watch('sass/**/*.scss',['styles']);
    gulp.watch('js/**/*.js',['js']);
});
