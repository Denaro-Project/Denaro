@extends('layouts.app')

@section('title', 'Report a scam')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">
                    <h1 class="h3 mb-0">Report a Scam</h1>
                    <p class="text-muted mb-0">Help protect others by reporting suspicious activities</p>
                </div>
                <div class="card-body">
                    {{-- <form method="POST" action="{{ route('scam.report') }}"> --}}
                    <form method="POST" action="">
                        @csrf
                        
                        <!-- User Email (Required) -->
                        <div class="mb-3">
                            <label for="email" class="form-label">
                                Your Email Address <span class="text-danger">*</span>
                            </label>
                            <input type="email" 
                                   class="form-control @error('email') is-invalid @enderror" 
                                   name="email" 
                                   id="email" 
                                   value="{{ old('email') }}"
                                   required>
                            @error('email')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Type of Scam Dropdown -->
                        <div class="mb-3">
                            <label for="scam_type" class="form-label">Type of Scam</label>
                            <select class="form-select @error('scam_type') is-invalid @enderror" 
                                    name="scam_type" 
                                    id="scam_type">
                                <option value="">Select scam type...</option>
                                <option value="phishing" {{ old('scam_type') == 'phishing' ? 'selected' : '' }}>Phishing</option>
                                <option value="fake_investment" {{ old('scam_type') == 'fake_investment' ? 'selected' : '' }}>Fake Investment</option>
                                <option value="romance_scam" {{ old('scam_type') == 'romance_scam' ? 'selected' : '' }}>Romance Scam</option>
                                <option value="tech_support" {{ old('scam_type') == 'tech_support' ? 'selected' : '' }}>Tech Support Scam</option>
                                <option value="lottery_prize" {{ old('scam_type') == 'lottery_prize' ? 'selected' : '' }}>Lottery/Prize Scam</option>
                                <option value="identity_theft" {{ old('scam_type') == 'identity_theft' ? 'selected' : '' }}>Identity Theft</option>
                                <option value="crypto_scam" {{ old('scam_type') == 'crypto_scam' ? 'selected' : '' }}>Cryptocurrency Scam</option>
                                <option value="other" {{ old('scam_type') == 'other' ? 'selected' : '' }}>Other</option>
                            </select>
                            @error('scam_type')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Custom Scam Type Input (shown when "Other" is selected) -->
                        <div class="mb-3" id="custom_scam_type_div" style="display: none;">
                            <label for="custom_scam_type" class="form-label">Please specify the type of scam</label>
                            <input type="text" 
                                   class="form-control @error('custom_scam_type') is-invalid @enderror" 
                                   name="custom_scam_type" 
                                   id="custom_scam_type"
                                   value="{{ old('custom_scam_type') }}"
                                   placeholder="Enter the type of scam">
                            @error('custom_scam_type')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Scammer's Name/Pseudonym -->
                        <div class="mb-3">
                            <label for="scammer_name" class="form-label">Scammer's Name/Pseudonym</label>
                            <input type="text" 
                                   class="form-control @error('scammer_name') is-invalid @enderror" 
                                   name="scammer_name" 
                                   id="scammer_name"
                                   value="{{ old('scammer_name') }}"
                                   placeholder="Enter the scammer's name or pseudonym">
                            @error('scammer_name')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Scammer's Phone Number -->
                        <div class="mb-3">
                            <label for="scammer_phone" class="form-label">Scammer's Phone Number</label>
                            <input type="tel" 
                                   class="form-control @error('scammer_phone') is-invalid @enderror" 
                                   name="scammer_phone" 
                                   id="scammer_phone"
                                   value="{{ old('scammer_phone') }}"
                                   placeholder="Enter the scammer's phone number">
                            @error('scammer_phone')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Scam URL -->
                        <div class="mb-3">
                            <label for="scam_url" class="form-label">Scam URL/Website</label>
                            <input type="url" 
                                   class="form-control @error('scam_url') is-invalid @enderror" 
                                   name="scam_url" 
                                   id="scam_url"
                                   value="{{ old('scam_url') }}"
                                   placeholder="https://example.com">
                            @error('scam_url')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Scam Contents -->
                        <div class="mb-3">
                            <label for="scam_contents" class="form-label">Scam Contents/Description</label>
                            <textarea class="form-control @error('scam_contents') is-invalid @enderror" 
                                      name="scam_contents" 
                                      id="scam_contents" 
                                      rows="5"
                                      placeholder="Describe what happened, what the scammer said, or paste the scam message content">{{ old('scam_contents') }}</textarea>
                            @error('scam_contents')
                                <div class="invalid-feedback">{{ $message }}</div>
                            @enderror
                        </div>

                        <!-- Submit Button -->
                        <div class="d-grid">
                            <button type="submit" class="btn btn-primary btn-lg">
                                <i class="fas fa-exclamation-triangle me-2"></i>
                                Submit Report
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const scamTypeSelect = document.getElementById('scam_type');
        const customScamTypeDiv = document.getElementById('custom_scam_type_div');
        const customScamTypeInput = document.getElementById('custom_scam_type');

        function toggleCustomInput() {
            if (scamTypeSelect.value === 'other') {
                customScamTypeDiv.style.display = 'block';
                customScamTypeInput.required = true;
            } else {
                customScamTypeDiv.style.display = 'none';
                customScamTypeInput.required = false;
                customScamTypeInput.value = '';
            }
        }

        // Initial check
        toggleCustomInput();

        // Listen for changes
        scamTypeSelect.addEventListener('change', toggleCustomInput);
    });
</script>
@endsection


