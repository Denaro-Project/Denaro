<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\TrustAnalysisController;
use App\Http\Controllers\UserController;

Route::get('/', function () {
    return view('auth.authentication');
});

// Guest-friendly home route (used by 'Continue as Guest')
Route::get('/home', function () {
    return view('home');
});

Route::group(['prefix' => 'scam'], function () {
    Route::get('/report', function () {
        return view('scam.scam_report');
    })->name('scam.report');

    Route::get('/info', function () {
        return view('scam.scam_info');
    })->name('scam.info');
});

Route::get('/trust-analysis', function () {
    return view('trust_analysis');
});
Route::post('/trust-analyze', [TrustAnalysisController::class, 'analyze'])->name('trust.analyze');


Route::controller(UserController::class)->group(function () {
    Route::get('/authenticate', 'authenticate')->name('authenticate');
    Route::get('/register', 'register')->name('register');
    Route::get('/login', 'login')->name('login');
    Route::post('/register', 'handleRegister')->name('register.post');
    Route::post('/login', 'handleLogin')->name('login.post');
    Route::post('/logout', 'logout')->name('logout');
});