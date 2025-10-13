
@extends('layouts.app')

@section('title', 'Web Trust Analysis Tool')

@section('content')
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card shadow-sm">
                    <div class="card-header bg-transparent border-bottom">
                        <h1 class="h4 mb-0">Web Trust Analysis Tool</h1>
                        <p class="text-muted mb-0 small">Enter a URL to perform a quick trust analysis of a website.</p>
                    </div>
                    <div class="card-body">
                        <form method="POST" action="{{ route('trust.analyze') }}" id="trustForm">
                            @csrf

                            <div class="form-floating mb-3">
                                <input type="url" 
                                       class="form-control @error('url') is-invalid @enderror" 
                                       name="url" 
                                       id="url" 
                                       placeholder="https://example.com"
                                       value="{{ old('url') }}"
                                       required>
                                <label for="url">Website URL</label>
                                @error('url')
                                    <div class="invalid-feedback">{{ $message }}</div>
                                @enderror
                            </div>

                            <div class="d-flex gap-2">
                                <button type="submit" class="btn btn-primary" id="analyzeBtn">
                                    <span id="analyzeSpinner" class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true" style="display:none"></span>
                                    Analyze
                                </button>
                                <a href="{{ url('/') }}" class="btn btn-outline-secondary">Back</a>
                            </div>
                        </form>

                        @isset($analysisResult)
                            <hr>
                            <h5 class="mb-3">Analysis Result</h5>

                            <div class="card mb-3">
                                <div class="card-body">
                                    @if(is_array($analysisResult))
                                        {{-- Try to show key fields if present --}}
                                        @if(isset($analysisResult['domain']))
                                            <p class="mb-1"><strong>Domain:</strong> {{ $analysisResult['domain'] }}</p>
                                        @endif
                                        @if(isset($analysisResult['score']))
                                            <p class="mb-1"><strong>Trust Score:</strong> {{ $analysisResult['score'] }}</p>
                                        @endif
                                        @if(isset($analysisResult['warnings']) && count($analysisResult['warnings']))
                                            <p class="mb-1"><strong>Warnings:</strong></p>
                                            <ul>
                                                @foreach($analysisResult['warnings'] as $w)
                                                    <li>{{ $w }}</li>
                                                @endforeach
                                            </ul>
                                        @endif
                                    @endif

                                    <details>
                                        <summary class="small text-muted">Raw output</summary>
                                        <pre class="small bg-light p-2 rounded">{{ print_r($analysisResult, true) }}</pre>
                                    </details>
                                </div>
                            </div>
                        @endisset
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('trustForm');
            const btn = document.getElementById('analyzeBtn');
            const spinner = document.getElementById('analyzeSpinner');

            if (form && btn) {
                form.addEventListener('submit', function() {
                    btn.setAttribute('disabled', 'disabled');
                    if (spinner) spinner.style.display = 'inline-block';
                });
            }
        });
    </script>

@endsection


