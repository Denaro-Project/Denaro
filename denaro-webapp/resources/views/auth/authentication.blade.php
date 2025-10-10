@extends('layouts.app')
@section('title', 'Authentication')

@section('content')
    <h1 class="h4 mb-4">Authentication</h1>

    <ul class="nav nav-tabs" id="authTabs" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link active" id="login-tab" data-bs-toggle="tab" data-bs-target="#login-pane" type="button" role="tab" aria-controls="login-pane" aria-selected="true">Login</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="register-tab" data-bs-toggle="tab" data-bs-target="#register-pane" type="button" role="tab" aria-controls="register-pane" aria-selected="false">Register</button>
        </li>
    </ul>

    <div class="tab-content p-3 border border-top-0 rounded-bottom bg-white" id="authTabsContent">
        <div class="tab-pane fade show active" id="login-pane" role="tabpanel" aria-labelledby="login-tab">
            <form method="POST" action="{{ route('login.post') }}" class="row g-3">
                @csrf
                <div class="col-12">
                    <label for="login_email" class="form-label">Email</label>
                    <input type="email" class="form-control" id="login_email" name="email" required autofocus>
                </div>
                <div class="col-12">
                    <label for="login_password" class="form-label">Password</label>
                    <input type="password" class="form-control" id="login_password" name="password" required>
                </div>
                <div class="col-12 d-flex align-items-center justify-content-between">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="1" id="remember" name="remember">
                        <label class="form-check-label" for="remember">Remember me</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Login</button>
                </div>
            </form>
        </div>

        <div class="tab-pane fade" id="register-pane" role="tabpanel" aria-labelledby="register-tab">
            <form method="POST" action="{{ route('register.post') }}" class="row g-3">
                @csrf
                <div class="col-12">
                    <label for="name" class="form-label">Name</label>
                    <input type="text" class="form-control" id="name" name="name" required>
                </div>
                <div class="col-12">
                    <label for="email" class="form-label">Email</label>
                    <input type="email" class="form-control" id="email" name="email" required>
                </div>
                <div class="col-12">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" class="form-control" id="password" name="password" required>
                </div>
                <div class="col-12">
                    <label for="password_confirmation" class="form-label">Confirm Password</label>
                    <input type="password" class="form-control" id="password_confirmation" name="password_confirmation" required>
                </div>
                <div class="col-12 text-end">
                    <button type="submit" class="btn btn-success">Create account</button>
                </div>
            </form>
        </div>
    </div>
@endsection