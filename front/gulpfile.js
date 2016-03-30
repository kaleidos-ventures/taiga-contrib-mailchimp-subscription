var gulp = require('gulp');
var $ = require('gulp-load-plugins')();

var paths = {
    jade: 'partials/*.jade',
    coffee: 'coffee/*.coffee',
    dist: 'dist/'
};

gulp.task('copy-config', function() {
    return gulp.src('mailchimp-subscription.json')
        .pipe(gulp.dest(paths.dist));
});

gulp.task('compile-jade', function() {
    return gulp.src(paths.jade)
        .pipe($.plumber())
        .pipe($.cached('jade'))
        .pipe($.jade({pretty: true}))
        .pipe($.remember('jade'))
        .pipe(gulp.dest(paths.dist));
});

gulp.task('compile-coffee', function() {
    return gulp.src(paths.coffee)
        .pipe($.plumber())
        .pipe($.cached('coffee'))
        .pipe($.coffee())
        .pipe($.remember('coffee'))
        .pipe($.concat('mailchimp-subscription.js'))
        .pipe($.uglify({mangle:false, preserveComments: false}))
        .pipe(gulp.dest(paths.dist));
});

gulp.task('watch', function() {
    gulp.watch([paths.jade], ['compile-jade']);
    gulp.watch([paths.coffee], ['compile-coffee']);
});

gulp.task('default', ['copy-config', 'compile-jade', 'compile-coffee', 'watch']);
gulp.task('build', ['copy-config', 'compile-jade', 'compile-coffee']);
