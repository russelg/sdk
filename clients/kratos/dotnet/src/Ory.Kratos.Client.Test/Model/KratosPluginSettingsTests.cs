/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.0.0-alpha.38
 * Contact: hi@ory.sh
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using Xunit;

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using Ory.Kratos.Client.Api;
using Ory.Kratos.Client.Model;
using Ory.Kratos.Client.Client;
using System.Reflection;
using Newtonsoft.Json;

namespace Ory.Kratos.Client.Test.Model
{
    /// <summary>
    ///  Class for testing KratosPluginSettings
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the model.
    /// </remarks>
    public class KratosPluginSettingsTests : IDisposable
    {
        // TODO uncomment below to declare an instance variable for KratosPluginSettings
        //private KratosPluginSettings instance;

        public KratosPluginSettingsTests()
        {
            // TODO uncomment below to create an instance of KratosPluginSettings
            //instance = new KratosPluginSettings();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of KratosPluginSettings
        /// </summary>
        [Fact]
        public void KratosPluginSettingsInstanceTest()
        {
            // TODO uncomment below to test "IsType" KratosPluginSettings
            //Assert.IsType<KratosPluginSettings>(instance);
        }


        /// <summary>
        /// Test the property 'Args'
        /// </summary>
        [Fact]
        public void ArgsTest()
        {
            // TODO unit test for the property 'Args'
        }
        /// <summary>
        /// Test the property 'Devices'
        /// </summary>
        [Fact]
        public void DevicesTest()
        {
            // TODO unit test for the property 'Devices'
        }
        /// <summary>
        /// Test the property 'Env'
        /// </summary>
        [Fact]
        public void EnvTest()
        {
            // TODO unit test for the property 'Env'
        }
        /// <summary>
        /// Test the property 'Mounts'
        /// </summary>
        [Fact]
        public void MountsTest()
        {
            // TODO unit test for the property 'Mounts'
        }

    }

}
