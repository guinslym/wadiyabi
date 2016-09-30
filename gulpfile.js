'use strict';

// Load npm modules
var gulp = require('gulp');
var concat = require('gulp-concat');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');
var shell = require('gulp-shell');

// Sass
gulp.task('style:sass', function() {
  return gulp.src(['./src/static/src/styles/main.scss'])
    .pipe(sourcemaps.init())
      .pipe(sass({ outputStyle: 'compressed' }))
      .pipe(concat('main.min.css'))
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest('./src/static/dist/css/'));
});

// Javascript
gulp.task('scripts:js', function() {
  return gulp.src(['./src/static/src/js/**/*.js'])
    .pipe(sourcemaps.init())
      .pipe(concat('main.min.js'))
      .pipe(uglify())
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest('./src/static/dist/js/'));
});

// Watches
gulp.task('watch', function() {
  gulp.watch('./src/static/src/styles/**/*.*', ['style:sass']);
  gulp.watch('./src/static/src/js/**/*.js', ['scripts:js']);
});

// Sphinx
// Nota, al ejecutar tanto 'build-docs' como 'sphinx', se ha de estar en un entorno
// virtual con sphinx o dara error.
gulp.task('build-docs', shell.task('make html', {cwd: './docs'}));

// Watch sphinx
gulp.task('sphinx', ['build-docs'], function() {
  gulp.watch('./docs/**/*.rst', ['build-docs']);
});

// Default
gulp.task('default', ['style:sass', 'scripts:js', 'watch']);
