@extends('layouts.app')
@section('title', 'Upload Image')

@section('content')
    <h1>Upload Image</h1>
    <div class="card" style="margin-top: 1rem;">
        <div class="card-body">
            @if(session('success'))
                <div class="alert alert-success">{{ session('success') }}</div>
                @if(session('path'))
                    <p>File: <a href="{{ asset('storage/' . session('path')) }}" target="_blank">{{ session('path') }}</a></p>
                    <img src="{{ asset('storage/' . session('path')) }}" alt="uploaded" class="img-fluid" style="max-width:300px;">
                @endif
            @endif

            @if($errors->any())
                <div class="alert alert-danger">
                    <ul class="mb-0">
                        @foreach($errors->all() as $err)
                            <li>{{ $err }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

            <form method="POST" action="{{ route('upload.image') }}" enctype="multipart/form-data">
                @csrf
                <div class="mb-3">
                    <label for="imageFile" class="form-label">Select Image (max 2MB)</label>
                    <input type="file" class="form-control" id="imageFile" name="imageFile" accept="image/*" required>
                </div>
                <button type="submit" class="btn btn-primary">Upload</button>
            </form>
        </div>
    </div>
@endsection